from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locdata', views.locdata, name="locdata"),
]
