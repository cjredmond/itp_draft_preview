from django.conf.urls import url
from django.contrib import admin
from player.views import PlayerDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^player/(?P<pk>\d+)/$', PlayerDetailView.as_view(), name='player_detail_view'),
]
