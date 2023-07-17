# Generated by Django 4.2 on 2023-05-25 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendas', '0009_remove_agendas_personnes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendas',
            name='medecins',
        ),
        migrations.AddField(
            model_name='agendas',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', related_query_name='agenda', to=settings.AUTH_USER_MODEL),
        ),
    ]