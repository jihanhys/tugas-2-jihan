from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_json_by_id
from mywatchlist.views import show_all

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    #path('xml/', show_xml, name='show_xml'),
    #path('json/', show_json, name='show_json'),
    #path('html/', show_watchlist, name='show_watchlist'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('<str:type>', show_all, name='show_all'),
]