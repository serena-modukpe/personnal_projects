from django.db import models
from agendas.models import Agendas
from authentication.models import Users
from specialites.models import Specialites
from statut.models import Statut

# Create your models here.
from django.db import models

class Rendezvous(models.Model):
    
    agendas = models.ForeignKey(Agendas, on_delete=models.CASCADE, to_field='id',
                            related_name='rendezvous',
                            related_query_name='rendezvous', null=True)

    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, to_field='id',
                                related_name='rendezvous',
                                related_query_name='rendezvous', null=True)

    users = models.ForeignKey(Users,  on_delete=models.CASCADE, to_field='id',
                             related_name='rendezvous',
                            related_query_name='rendezvous', null=True)

    specialites = models.ForeignKey(Specialites,  on_delete=models.CASCADE, to_field='id',
                             related_name='rendezvous',
                            related_query_name='rendezvous', null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.TextField(null=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    updated_by = models.TextField(null=True)


 






    