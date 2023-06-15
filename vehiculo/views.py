from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm
from .models import Car
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='iniciar_sesion')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='iniciar_sesion')
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            print('hola')
            form.save()
            #return redirect('car_list')  # Redirecciona a la lista de carros después de guardar
    else:
        print('HOla2')
        form = CarForm()
    
    return render(request, 'form.html', {'form': form})

@login_required(login_url='iniciar_sesion')
def list_car(request):
    vehiculos = Car.objects.all()
    return render(request, 'list_car.html', {'vehiculos':vehiculos})