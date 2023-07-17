from django.db import models
from consultations.models import Consultations
from dossierpatients.models import Dossierpatients

# Create your models here.
class Consultationpatients(models.Model):

    consultations = models.ForeignKey(Consultations, on_delete=models.CASCADE, to_field='id', related_name='consultationpatients', related_query_name='consultationpatient', null=True, )

    dossierpatients = models.ForeignKey(Dossierpatients, on_delete=models.CASCADE, to_field='id', related_name='consultationpatients', related_query_name='consultationpatient', null=True)

    observation = models.TextField()
    recommandation = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)