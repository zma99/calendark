from django.shortcuts import render, redirect
from .models import Usuario
from .forms import userForm

def home(request):
    return render(request, 'home.html')

def new_user(request):
    if request.method == 'GET':
        form = userForm()
        contexto = {
            'form':form
        }
    if request.method == 'POST':
        form = userForm(request.POST)
        print(form)
        contexto = {
            'form':form
        }
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'new_user.html', contexto)

def users_list(request):
    usuarios = Usuario.objects.all()          #select * from Usuario
    contexto = {
        'usuarios':usuarios
    }
    return render(request, 'users_list.html', contexto)

def login(request):
    if request.method == 'GET':
        form = userForm()
        contexto = {
            'Nombre de usuario':form.username,
            'Contraseña':form.password
        }
    if request.method == 'POST':
        form = userForm(request.POST)
        print(form)
        contexto = {
            'form':form
        }
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'login.html', contexto)