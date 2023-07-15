# Generated by Django 4.1.7 on 2023-04-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crearservicio',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='crearservicio',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='crearservicio',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='crearservicio',
            name='provincia',
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='apartamen_suite_proyec',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='calle_proyec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='ciudad_proyec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='descripcion_proyecto',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='numero_proyec',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='provincia_proyec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='crearservicio',
            name='sector_proyec',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='crearservicio',
            name='comision_vendedor',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='crearservicio',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='crearservicio',
            name='telefono',
            field=models.CharField(blank=True, default='000 000 0000', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='crearservicio',
            name='whatsapp',
            field=models.CharField(blank=True, default='000 000 0000', max_length=20, null=True),
        ),
    ]
