from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locdata/', views.locdata, name="locdata"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name="profile")
]
