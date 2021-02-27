from django.shortcuts import render, redirect
from .models import Usuario
from .forms import userForm

def home(request):
    usuarios = Usuario.objects.all()          #select * from Usuario
    contexto = {
        'usuarios':usuarios
    }
    return render(request, 'home.html', contexto)

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