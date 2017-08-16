from django.conf.urls import url
from django.contrib import admin
from player.views import PlayerDetailView, PlayerListView, SchoolListView
from user_auth.views import DashboardView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^player/(?P<pk>\d+)/$', PlayerDetailView.as_view(), name='player_detail_view'),
    url(r'^$', DashboardView.as_view(), name='dashboard_view'),
    url(r'^school-list/$', SchoolListView.as_view(), name='school_list_view'),
    url(r'^player-list/$', PlayerListView.as_view(), name='player_list_view'),
]
