from django.urls import path
from todolist.views import show_task, add, register, login_user, logout_user,add_task, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='create-task'),
    path('/json', show_json, name='show_json'),
    path('/add', add, name='add'),
]