# Generated by Django 4.1.5 on 2023-05-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0011_alter_crearproyecto_codigo_unico_proyect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearproyecto',
            name='codigo_unico_proyect',
            field=models.CharField(blank=True, editable=False, max_length=12, null=True, unique=True, verbose_name='Código Único'),
        ),
    ]
