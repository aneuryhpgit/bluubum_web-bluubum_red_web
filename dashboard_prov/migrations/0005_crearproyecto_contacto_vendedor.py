# Generated by Django 4.1.7 on 2023-04-13 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vend_config_inic', '0003_metodo_pago_vendedor_nombre_banco_and_more'),
        ('dashboard_prov', '0004_crearproyecto_codigo_unico_proyect_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crearproyecto',
            name='contacto_vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vend_config_inic.contacto_vendedor'),
        ),
    ]
