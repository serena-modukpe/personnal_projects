from django.db import models
from authentication.models import Users

# Create your models here.

class Personnes(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    telephone = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    ddn = models.DateField()	
    adresse = models.CharField(max_length=255)
    users = models.ForeignKey( Users, on_delete=models.CASCADE, to_field='id', related_name='personnes', related_query_name='personne', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)