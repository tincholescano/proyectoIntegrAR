# Generated by Django 5.1.2 on 2024-11-03 23:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0006_area_ubicacion_consultaespecifica'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('nucleo_familiar', models.CharField(blank=True, max_length=100)),
                ('respuesta', models.TextField(blank=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='consultas.area')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='consultas.ubicacion')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]