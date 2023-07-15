# Generated by Django 4.1.7 on 2023-04-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil_proveedor', '0004_alter_profile_proveedor_codigo_unico_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_proveedor',
            name='anio_nacimiento',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Año de Nacimiento'),
        ),
        migrations.AddField(
            model_name='profile_proveedor',
            name='dia_nacimiento',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Día de Nacimiento'),
        ),
        migrations.AddField(
            model_name='profile_proveedor',
            name='mes_nacimiento',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Mes de Nacimiento'),
        ),
    ]
