# Generated by Django 5.1.2 on 2024-11-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_add_default_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
    ]