from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core import serializers

from session_manager.forms import LocationDataForm, AddSessionForm
from session_manager.models import Player, Session, LocationData

import json
import random
import string

# Create your views here.


def index(request):
    return render(request, "session_manager/index.html")


def locdata(request):
    if request.method == "POST":
        form = LocationDataForm(request.POST)
        if form.is_valid():
            seskey = form.cleaned_data['session_key']
            session = get_object_or_404(Session, key=seskey)
            devid = form.cleaned_data['player_key']
            times = form.cleaned_data['time_list']
            locs = form.cleaned_data['loc_list']
            if len(times) != len(locs):
                return render(request, "session_manager/locdata.html", {})

            player_query = Player.objects.filter(device_id=devid, session__key=seskey)
            locdata = []
            for i in range(len(times)):
                x, y, z = locs[i].split(" ")
                ld = LocationData.objects.create(timestamp=times[i], x=x, y=y, z=z)
                locdata += [ld]

            player = None
            # if new player
            if not player_query:
                player = Player(device_id=devid)
                player.save()
            else:
                player = player_query.first()
            for i in range(len(locdata)):
                player.datapoints.add(locdata[i])
            player.save()
            session.players.add(player)
            session.save()
    # if not POST
    else:
        form = LocationDataForm()

    context = {
        "form": form
    }

    return render(request, "session_manager/locdata.html", context)


# Basically makes nesting work properly as
# otherwise, player and location data would 
# only be referneced by index and not contian actual data.
def get_json_from_session(s, pk):
    # Fix session json data
    q = list(s)
    json_str = serializers.serialize("json", q)
    j = json.loads(json_str)
    j = j[0]["fields"]

    # Fix player json data
    del j["players"]
    
    players_query = Player.objects.filter(session=pk)
    players_query = list(players_query)
    player_data = serializers.serialize("json", players_query)
    player_data = json.loads(player_data)
    j["playerData"] = []
    for player in player_data:
        # fix location data and finalize player fix
        location_query = LocationData.objects.filter(player=player["pk"])
        location_query = list(location_query)
        location_data = serializers.serialize("json", location_query)
        location_data = json.loads(location_data)

        cleaned_locdata = []
        for locdata in location_data:
            cleaned_locdata += [locdata["fields"]]

        player["fields"]["datapoints"] = cleaned_locdata
        j["playerData"] += [player["fields"]]

    json_str = json.dumps(j)
    return json_str


def generate_random_key(length):
    palette = string.ascii_letters + string.digits
    while True:
        key = "".join([random.choice(palette) for i in range(length)])
        search = Session.objects.filter(key=key)
        if not search:
            return key


def profile(request):
    if request.user.is_authenticated:
        context = {
            "session_list": Session.objects.all(),
            "form":AddSessionForm()
        }
        if request.method == "POST":
            form = AddSessionForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                s = Session(name=name, key=generate_random_key(20))
                s.save()
                HttpResponseRedirect('/')
                
        elif request.method == "GET":
            pk = request.GET.get("download")
            if pk != None:
                s = Session.objects.filter(pk=pk)
                if s:
                    json_str = get_json_from_session(s, pk)
                    response = HttpResponse(json_str, content_type="application/json")
                    response["Content-Disposition"] = f"attachment; filename={s.first().name}.json"
                    return response

            else:
                pk = request.GET.get("delete")
                if pk != None:
                    s = Session.objects.filter(pk=pk).delete()

        return render(request, "session_manager/profile.html", context)
    return redirect("login")
