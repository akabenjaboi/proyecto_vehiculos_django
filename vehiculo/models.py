from django.db import models
from django.core.exceptions import ValidationError


def no_negative_validator(value):
    if value < 0:
        raise ValidationError('El número no puede ser negativo.')

class Car(models.Model):
    BRAND_CHOICES = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )
    
    CATEGORY_CHOICES = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )
    
    marca = models.CharField(max_length=20, choices=BRAND_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Particular')
    precio = models.IntegerField(validators=[no_negative_validator])
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("visualizar_vehiculos","visualizar_vehiculos"),
        )
    

    def __str__(self):
        return f"{self.marca} {self.modelo}"

