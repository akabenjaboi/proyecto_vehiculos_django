from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import User, Permission, Group

# Create your views here.

@unauthenticated_user
def registrar(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            '''
            # Asignar el permiso 'visualizar_catalogo' al usuario
            permiso = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permiso)
            '''

            '''
            permiso, created = Permission.objects.get_or_create(
                codename='visualizar_catalogo',
                name='Visualizar catálogo',
            )

            user.user_permissions.add(permiso)
            '''
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, f"La cuenta '{username}' fue creada exitosamente")

            return redirect('iniciar_sesion')
        else:
            messages.error(request, "La cuenta no pudo ser creada. Asegúrate de rellenar todos los campos y, si el problema persiste, intenta con otro usuario.")

    context = {'form': form}
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
