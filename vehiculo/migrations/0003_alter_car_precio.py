# Generated by Django 4.0.5 on 2023-06-14 18:35

from django.db import migrations, models
import vehiculo.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_rename_category_car_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='precio',
            field=models.IntegerField(validators=[vehiculo.models.no_negative_validator]),
        ),
    ]