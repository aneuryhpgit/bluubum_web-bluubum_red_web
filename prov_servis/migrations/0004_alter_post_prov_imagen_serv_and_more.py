# Generated by Django 4.1.5 on 2023-04-23 06:44

from django.db import migrations, models
import prov_servis.models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_servis', '0003_alter_servicio_prov_descripcion_serv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_prov',
            name='imagen_serv',
            field=models.ImageField(default='NULL', upload_to=prov_servis.models.imgpost_directory_path),
        ),
        migrations.AlterField(
            model_name='post_prov',
            name='imagen_serv_cuatro',
            field=models.ImageField(default='NULL', upload_to=prov_servis.models.imgpost_directory_path),
        ),
        migrations.AlterField(
            model_name='post_prov',
            name='imagen_serv_dos',
            field=models.ImageField(default='NULL', upload_to=prov_servis.models.imgpost_directory_path),
        ),
        migrations.AlterField(
            model_name='post_prov',
            name='imagen_serv_tres',
            field=models.ImageField(default='NULL', upload_to=prov_servis.models.imgpost_directory_path),
        ),
    ]
