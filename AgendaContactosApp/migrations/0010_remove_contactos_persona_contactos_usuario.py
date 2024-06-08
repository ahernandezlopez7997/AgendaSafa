# Generated by Django 4.2.13 on 2024-06-06 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaContactosApp', '0009_rename_usuarios_contactos_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactos',
            name='persona',
        ),
        migrations.AddField(
            model_name='contactos',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]