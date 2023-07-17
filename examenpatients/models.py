from django.db import models
from dossierpatients.models import Dossierpatients
from authentication.models import Users
from type_examens.models import Type_examens

# Create your models here.
class Examenpatients(models.Model):
    description = models.TextField()
    resultat = models.TextField()
    dossierpatients = models.ForeignKey(Dossierpatients, on_delete=models.CASCADE, to_field='id', related_name='examenpatients', related_query_name='examenpatient', null=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='id', related_name='examenpatients', related_query_name='examenpatient', null=True)
    type_examens = models.ForeignKey(Type_examens, on_delete=models.CASCADE, to_field='id', related_name='examenpatients', related_query_name='examenpatient', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)