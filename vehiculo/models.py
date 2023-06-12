from django.db import models

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
    
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='Ford')
    model = models.CharField(max_length=100)
    body_serial = models.CharField(max_length=50)
    engine_serial = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Particular')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.brand} {self.model}"
