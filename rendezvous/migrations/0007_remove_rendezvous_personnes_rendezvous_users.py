# Generated by Django 4.2.1 on 2023-05-24 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rendezvous', '0006_alter_rendezvous_agendas_alter_rendezvous_personnes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendezvous',
            name='personnes',
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', related_query_name='rendezvous', to=settings.AUTH_USER_MODEL),
        ),
    ]
