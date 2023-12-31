# Generated by Django 4.2.1 on 2023-05-19 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0002_remove_consultations_date_remove_consultations_heure_and_more'),
        ('consultationpatients', '0002_alter_consultationpatients_consultations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationpatients',
            name='consultations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultationpatients', related_query_name='consultationpatient', to='consultations.consultations'),
        ),
    ]
