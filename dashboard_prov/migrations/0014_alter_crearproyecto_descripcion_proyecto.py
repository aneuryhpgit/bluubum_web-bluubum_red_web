# Generated by Django 4.1.5 on 2023-05-01 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0013_alter_crearproyecto_apartamen_suite_proyec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearproyecto',
            name='descripcion_proyecto',
            field=models.CharField(blank=True, max_length=1030, null=True),
        ),
    ]
