# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_bonus, show_watchlist
from mywatchlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat

# TODO: Implement Routings Here
app_name = 'my watchlist'

urlpatterns = [
    path('bonus/', show_bonus, name='show_bonus'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 


]
