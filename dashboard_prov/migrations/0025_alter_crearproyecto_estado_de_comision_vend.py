# Generated by Django 4.1.5 on 2023-05-09 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0024_crearproyecto_fecha_saldado_comis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearproyecto',
            name='estado_de_comision_vend',
            field=models.CharField(default='NULL', max_length=12),
        ),
    ]
