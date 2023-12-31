# Generated by Django 4.1.7 on 2023-04-25 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_vendedor', '0002_rename_codigo_unico_proveedor_profile_vendedor_codigo_unico_vendedor'),
        ('perfil_proveedor', '0005_profile_proveedor_anio_nacimiento_and_more'),
        ('dashboard_prov', '0007_crearproyecto_comision_prov'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_comision_vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_de_comision', models.CharField(default='Pendiente', max_length=30)),
                ('afiliacion_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servis_afiliacion_users', to='dashboard_prov.afiliacion')),
                ('proveedor_foren', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil_proveedor.profile_proveedor')),
                ('proyecto_foren', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard_prov.crearproyecto')),
                ('vendedor_foren', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login_vendedor.profile_vendedor')),
            ],
            options={
                'verbose_name': 'estado_comision_vendedores',
            },
        ),
    ]
