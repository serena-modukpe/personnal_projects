# Generated by Django 4.2.1 on 2023-05-17 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jours', '0001_initial'),
        ('agendas', '0005_agendas_medecins_agendas_personnes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendas',
            name='jours',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', related_query_name='agenda', to='jours.jours'),
        ),
    ]
