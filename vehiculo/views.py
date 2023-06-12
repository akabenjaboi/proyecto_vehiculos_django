from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm
from .models import Car

# Create your views here.

def index(request):
    return render(request, 'index.html')

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