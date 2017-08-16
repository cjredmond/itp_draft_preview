from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from player.models import Player
from report.models import Report


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['new_players'] = Player.objects.all().order_by('-id')[:10]
        context['new_reports'] = Report.objects.all().order_by('-id')[:10]
        return context
