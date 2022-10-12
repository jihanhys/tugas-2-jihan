from urllib import response
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TodoForm
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_task(request):
    task_data = Task.objects.filter(user=request.user)

    context = {
        'username': request.user,
        'task_list' : task_data,
    }
    return render(request, "todolist.html", context)

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data))

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        data = Task(user=request.user,title=title, description=description)
        data.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_task')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_task(request):
    form = TodoForm(request.POST or None)
    response = {
        'form':form,
        'username': request.user
    }
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todolist:show_task')
    return render(request, "create-task.html", response)