from django.shortcuts import render
from django.views.generic import DetailView
from player.models import Player

class PlayerDetailView(DetailView):
    model = Player
