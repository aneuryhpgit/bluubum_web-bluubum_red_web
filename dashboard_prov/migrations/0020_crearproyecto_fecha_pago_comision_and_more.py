# Generated by Django 4.1.5 on 2023-05-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_prov', '0019_alter_comisiones_vendedor_comision'),
    ]

    operations = [
        migrations.AddField(
            model_name='crearproyecto',
            name='fecha_pago_comision',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crearproyecto',
            name='fecha_pago_comision_vend',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crearproyecto',
            name='estado_de_comision_vend',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
