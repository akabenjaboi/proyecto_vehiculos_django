from django.db import models
from django.apps import AppConfig
from django.contrib.auth.models import Permission

"""
class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

    def ready(self):
        # Creo el permiso 'visualizar_catalogo'
        Permission.objects.get_or_create(
            codename='visualizar_catalogo',
            name='Puede visualizar Catálogo de Vehículos',
            content_type__app_label=self.label
        )
"""
