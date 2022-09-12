from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context  ={
        'item_catalog'  : data_catalog_item,
        'nama'          : 'Jihan Hanifah Yasmin',
        'npm'           : 2106701955
    }
    return render(request, "katalog.html", context)