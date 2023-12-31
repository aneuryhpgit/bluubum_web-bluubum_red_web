# Generated by Django 4.1.5 on 2023-05-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0014_alter_crearproyecto_descripcion_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearproyecto',
            name='apartamen_suite_proyec',
            field=models.CharField(blank=True, default='suite', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='calle_proyec',
            field=models.CharField(blank=True, default='calle', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='ciudad_proyec',
            field=models.CharField(blank=True, default='Ciudad', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='descripcion_proyecto',
            field=models.CharField(blank=True, default='Descripcion', max_length=1030, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='numero_proyec',
            field=models.CharField(blank=True, default='numero', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='provincia_proyec',
            field=models.CharField(blank=True, default='Provincia', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='sector_proyec',
            field=models.CharField(blank=True, default='Sector', max_length=50, null=True),
        ),
    ]
