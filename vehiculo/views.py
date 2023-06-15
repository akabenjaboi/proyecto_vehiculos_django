from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm
from .models import Car
from django.contrib.auth.decorators import login_required
from login.decorators import allowed_users
# Create your views here.

from django.shortcuts import render

@login_required(login_url='iniciar_sesion')
def index(request):
    context = {
        # Agrega los datos que deseas pasar a la plantilla 'index.html'
    }
    return render(request, 'index.html', context)

@login_required(login_url='iniciar_sesion')
@allowed_users(allowed_roles=['admin'])
def create_car(request):
    context = {}  # Puedes agregar datos adicionales al contexto si es necesario

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('car_list')
    else:
        form = CarForm()

    context['form'] = form  # Agrega el formulario al contexto
    return render(request, 'form.html', context)

@login_required(login_url='iniciar_sesion')
def list_car(request):
    vehiculos = Car.objects.all()
    context = {'vehiculos': vehiculos}  # Agrega los vehículos al contexto
    return render(request, 'list_car.html', context)
