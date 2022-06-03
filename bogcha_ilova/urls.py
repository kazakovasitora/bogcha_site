from django.urls import path
from .views import *

urlpatterns = [
    path('', bosh_sahifa, name='home'),
    path('about/', about, name='about'),
    path('blok/', blok, name='blok'),
    path('klas/', klas, name='class'),
    path('kontakt/', kontakt, name='contakt'),
    path('gallery/', galery, name='gallery'),
    path('sing/', sing, name='single'),
    path('team/', team1, name='team'),
]