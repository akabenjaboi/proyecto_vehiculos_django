from django.urls import path 
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('logout/', views.logoutUser, name='logout')
]