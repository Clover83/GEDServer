from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<uuid:seskey>/renew', views.locdata, name="locdata"),
]
