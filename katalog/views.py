from django.shortcuts import render
from katalog.models import CatalogItem


# TODO : Create your views here.
def katalog_view(request):
    daftar_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': daftar_katalog,
        'name': 'Shafa Trivia Ezananda',
        'id': '2206026971'
    }
    return render(request, "katalog.html", context)
