from django.shortcuts import render
from django.views.generic import DetailView, ListView
from player.models import Player, School

class PlayerDetailView(DetailView):
    model = Player

class PlayerListView(ListView):
    model = Player

class SchoolListView(ListView):
    model = School
