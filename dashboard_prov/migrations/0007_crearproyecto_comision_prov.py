# Generated by Django 4.1.7 on 2023-04-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0006_remove_crearproyecto_contacto_vendedor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crearproyecto',
            name='comision_prov',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
