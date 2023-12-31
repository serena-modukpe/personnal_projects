# Generated by Django 4.2 on 2023-05-16 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('type_examens', '0001_initial'),
        ('dossierpatients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examenpatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('resultat', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.TextField(null=True)),
                ('dossierpatients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examenpatients', related_query_name='examenpatient', to='dossierpatients.dossierpatients')),
                ('type_examens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examenpatients', related_query_name='examenpatient', to='type_examens.type_examens')),
            ],
        ),
    ]
