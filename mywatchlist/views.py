from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import WatchlistItem

# Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'name': 'safa',
        'id': '2206026971'
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def show_bonus (request):
    data = WatchlistItem.objects.all()
    counter_watched = 0
    counter_unwatched = 0
    result = False

    for item in data:
        if item.watched:
            counter_watched +=1
        else:
            counter_unwatched +=1

    if counter_watched >= counter_unwatched:
        result = True

    context = {
        'watched_more' : result,
    }

    return render(request, "watchlist_bonus.html", context)