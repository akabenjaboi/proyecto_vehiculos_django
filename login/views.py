from django.shortcuts import render

# Create your views here.

def registrar(request):
    if request.method == "GET":
        return render(request, "registrar.html")

def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "iniciar_sesion.html")