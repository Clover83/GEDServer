from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from session_manager.forms import LocationDataForm 
#from session_manager.models import Player

# Create your views here.


def index(request):
    return HttpResponse("Hello world. Welcome to session_manager.")


def locdata(request):
    if request.method == "POST":
        form = LocationDataForm(request.POST)
        if form.is_valid():
            seskey = form.cleaned_data['session_key']
            session = get_object_or_404(Session, key=seskey)
            devid = form.cleaned_data['player_key']
            times = form.cleaned_data['time_list']
            locs = form.cleaned_data['loc_list']

            player_query = Player.objects.filter(device_id=devid, session__key=seskey)
            locdata = []
            for i in range(len(times)):
                lat, lon = locs[i].split(" ")
                ld = LocationData.objects.create(timestamp=times[i], latitude=lat, longitude=lon)
                locdata +=[ld]

            player = None
            # if new player
            if not player_query:
                player = Player(device_id=devid)
            else:
                player = player_query.first()

            for i in range(len(locdata)):
                p.datapoints.add(locdata[i])
            player.save()


    return HttpResponse("LOCDATA PAGE");



