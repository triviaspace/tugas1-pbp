from django.shortcuts import render
from katalog.models import CatalogItem


# TODO : Create your views here.
def katalog_view(request):
    daftar_item = CatalogItem.objects.all()
    context = {
        'list_item': daftar_item,
        'Nama': 'Shafa Trivia Ezananda',
        'ID': '2206026971'
    }
    return render(request, "katalog.html", context)
