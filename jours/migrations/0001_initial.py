# Generated by Django 4.2 on 2023-05-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.TextField(null=True)),
            ],
        ),
    ]