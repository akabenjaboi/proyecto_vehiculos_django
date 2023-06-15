from django.contrib import admin
from django.urls import path, include
from vehiculo.views import index

urlpatterns = [
    path('inicio/', index, name='inicio'),
    path('admin/', admin.site.urls),
    path('', include('vehiculo.urls')),
    path('', include('login.urls'))
]
