# Generated by Django 4.2.1 on 2023-05-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statut', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statut',
            name='libelle',
            field=models.CharField(choices=[('Actif', 'Actif'), ('Inactif', 'Inactif')], default='Inactif', max_length=255, unique=True),
        ),
    ]
