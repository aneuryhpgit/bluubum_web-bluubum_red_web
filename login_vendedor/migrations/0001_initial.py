# Generated by Django 4.1.7 on 2023-04-09 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_unico_proveedor', models.CharField(editable=False, max_length=7, unique=True, verbose_name='Código Único')),
                ('image', models.ImageField(blank=True, default='blank-profile-picture-gb46548963_1280.png', null=True, upload_to='imglogo', verbose_name='Profile Image')),
                ('nombre_empresa', models.CharField(default='Nombre de mi empresa', max_length=50)),
                ('configured', models.BooleanField(default=False)),
                ('politicas', models.BooleanField(default=False)),
                ('anio_nacimiento', models.PositiveIntegerField(blank=True, null=True, verbose_name='Año de Nacimiento')),
                ('mes_nacimiento', models.PositiveIntegerField(blank=True, null=True, verbose_name='Mes de Nacimiento')),
                ('dia_nacimiento', models.PositiveIntegerField(blank=True, null=True, verbose_name='Día de Nacimiento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]