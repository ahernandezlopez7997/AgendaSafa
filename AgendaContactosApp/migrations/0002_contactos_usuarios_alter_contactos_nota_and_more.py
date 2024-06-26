# Generated by Django 5.0.6 on 2024-06-03 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaContactosApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='usuarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AgendaContactosApp.usuarios'),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='nota',
            field=models.CharField(default='Sin nota', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
