from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from session_manager.forms import LocationDataForm 
from session_manager.models import Player

# Create your views here.


def index(request):
    return HttpResponse("Hello world. Welcome to session_manager.")


def locdata(request, seskey):
    session = get_object_or_404(Session, key=seskey)

    if request.method == "POST":
        form = LocationDataForm(request.POST)
        if form.is_valid():
           # get players in session
           if form.cleaned_data['player_key']:
               pass

    return HttpResponse("LOCDATA PAGE");



