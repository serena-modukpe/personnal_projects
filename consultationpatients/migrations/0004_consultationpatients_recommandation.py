# Generated by Django 4.2 on 2023-05-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultationpatients', '0003_alter_consultationpatients_consultations'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationpatients',
            name='recommandation',
            field=models.TextField(null=True),
        ),
    ]