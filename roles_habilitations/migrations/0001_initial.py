# Generated by Django 4.2.1 on 2023-05-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roles', '0002_roles_description_roles_updated_at_roles_updated_by_and_more'),
        ('habilitations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desrolhab', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_by', models.DateTimeField(auto_now_add=True, null=True)),
                ('habilitations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles_habilitations', related_query_name='role_habilitation', to='habilitations.habilitations')),
                ('roles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles_habilitations', related_query_name='role_habilitation', to='roles.roles')),
            ],
        ),
    ]
