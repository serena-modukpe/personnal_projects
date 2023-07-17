from django.db import models
from personnes.models import Personnes
from specialites.models import Specialites

class Medecins(models.Model):
    nom= models.CharField (max_length=255, null=True)
    prenom= models.CharField (max_length=255, null=True)
    telephone= models.CharField(max_length=100, null=True)
    email= models.EmailField(null=True)
    adresse= models.CharField (max_length=255, null=True)

    personnes = models.ForeignKey(Personnes,  on_delete=models.CASCADE, to_field='id',
                             related_name='medecins',
                            related_query_name='medecin', null=True)

    specialites = models.ForeignKey(Specialites,  on_delete=models.CASCADE, to_field='id',
                             related_name='medecins',
                            related_query_name='medecin', null=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)

