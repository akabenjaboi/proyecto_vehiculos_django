# Generated by Django 4.0.5 on 2023-06-12 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='created_at',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='brand',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='model',
            new_name='modelo',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='modified_at',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='price',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='body_serial',
            new_name='serial_carroceria',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='engine_serial',
            new_name='serial_motor',
        ),
    ]
