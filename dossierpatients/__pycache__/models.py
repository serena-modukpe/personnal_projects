from django.db import models
from personnes.models import Personnes
# Create your models here.
class Dossierpatients(models.Model):
    personnes = models.ForeignKey(Personnes, on_delete=models.CASCADE, to_field='id', related_name='dossierpatients', related_query_name='dossierpatient', null=True)
    numero = models.IntegerField(unique= True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)