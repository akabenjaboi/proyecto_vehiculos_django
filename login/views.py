from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def registrar(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta '+ user + ' fue creada existosamente')

            return redirect('iniciar_sesion')

    context = {'form':form}
    return render(request, "registrar.html", context)

@unauthenticated_user
def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.info(request, 'Usuario o Contraseña incorrectas')
    return render(request, "iniciar_sesion.html")

def logoutUser(request):
    logout(request)
    return redirect('iniciar_sesion')
