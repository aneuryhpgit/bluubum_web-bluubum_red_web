# Generated by Django 4.1.5 on 2023-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_servis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio_prov',
            name='descripcion_serv',
            field=models.CharField(blank=True, default='NULL', max_length=250, null=True),
        ),
    ]
