# Generated by Django 4.1.7 on 2023-03-30 15:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('perfil_proveedor', '0002_confirmacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_proveedor',
            name='codigo_unico_proveedor',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=7, unique=True, verbose_name='Código Único'),
        ),
    ]