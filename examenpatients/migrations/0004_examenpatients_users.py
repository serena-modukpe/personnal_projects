# Generated by Django 4.2 on 2023-06-02 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examenpatients', '0003_alter_examenpatients_resultat'),
    ]

    operations = [
        migrations.AddField(
            model_name='examenpatients',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examenpatients', related_query_name='examenpatient', to=settings.AUTH_USER_MODEL),
        ),
    ]
