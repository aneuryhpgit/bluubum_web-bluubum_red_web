# Generated by Django 4.1.7 on 2023-04-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vend_config_inic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metodo_pago_vendedor',
            name='tipo_document_identificacion',
            field=models.CharField(blank=True, default='Cedula', max_length=15, null=True),
        ),
    ]
