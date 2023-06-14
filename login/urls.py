from django.urls import path 
from . import views

urlpatterns = [
    path('registrar/', views.registrar),
    path('iniciar_sesion/', views.iniciar_sesion),
]