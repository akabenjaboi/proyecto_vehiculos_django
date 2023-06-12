from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('form/', views.create_car, name='create_car'),
]