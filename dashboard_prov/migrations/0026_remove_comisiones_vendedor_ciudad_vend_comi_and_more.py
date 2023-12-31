# Generated by Django 4.1.5 on 2023-05-10 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vend_config_inic', '0003_metodo_pago_vendedor_nombre_banco_and_more'),
        ('dashboard_prov', '0025_alter_crearproyecto_estado_de_comision_vend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='ciudad_vend_comi',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='codigo_unico_proyecto',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='comision',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='direccion_vendedor_comi',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='metodo_cobro_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_banco_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_completo_id_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_proveedor_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_proyect_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_servicio_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='nombre_vendedor_comision',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='numero_cuenta_bancaria_vend',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='provincia_vend_comi',
        ),
        migrations.RemoveField(
            model_name='comisiones_vendedor',
            name='tipo_document_id_vend',
        ),
        migrations.AddField(
            model_name='comisiones_vendedor',
            name='direccion_comi_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direc_vend_comision_fk', to='vend_config_inic.direccion_vendedor'),
        ),
        migrations.AddField(
            model_name='comisiones_vendedor',
            name='metd_pg_vend_comi_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mtd_pago_vend_comision_fk', to='vend_config_inic.metodo_pago_vendedor'),
        ),
    ]
