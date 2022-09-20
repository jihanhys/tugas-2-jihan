from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    watchlist_data = MyWatchList.objects.all()

    sudah = 0
    belum = 0
    for o in watchlist_data:
        if o.watched == "Sudah ditonton":
            sudah +=1
        else:
            belum +=1

    context = {
        'watchlist_item'    : watchlist_data,
        'nama'              :"Jihan Hanifah Yasmin",
        'npm'               : 2106701955,
        'watched_count'     : sudah,
        'unwatched_count'   : belum
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
