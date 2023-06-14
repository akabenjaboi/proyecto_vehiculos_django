from django.urls import path 
from . import views

urlpatterns = [
    path('inicio/', views.index),
    path('vehiculos/add/', views.create_car, name='create_car'),
    path('vehiculos/list/', views.list_car),
]