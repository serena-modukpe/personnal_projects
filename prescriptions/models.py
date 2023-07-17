from django.db import models
from authentication.models import Users
from dossierpatients.models import Dossierpatients
# Create your models here.

class Prescriptions(models.Model):
    quantite = models.CharField(max_length=255) 
    possologie = models.CharField(max_length=255)
    medicament = models.CharField(max_length=255)
    categorie_prescription = models.CharField(max_length=255)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='id', related_name='prescriptions', related_query_name='prescription', null=True)
    dossierpatients = models.ForeignKey(Dossierpatients, on_delete=models.CASCADE, to_field='id', related_name='prescriptions', related_query_name='prescription', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)
