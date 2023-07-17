from django.db import models
from authentication.models import Users
from jours.models import Jours
from heures.models import Heures
from statut.models import Statut
from specialites.models import Specialites

class Agendas(models.Model):
    heures = models.ForeignKey(Heures,  on_delete=models.CASCADE, to_field='id',
                             related_name='agendas',
                            related_query_name='agenda', null=True)

    jours = models.ForeignKey(Jours,  on_delete=models.CASCADE, to_field='id',
                             related_name='agendas',
                            related_query_name='agenda', null=True)

    
    users = models.ForeignKey(Users,  on_delete=models.CASCADE, to_field='id',
                             related_name='agendas',
                            related_query_name='agenda', null=True )

    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, to_field='id',
                                related_name='agendas',
                                related_query_name='agenda', null=True)

    specialites = models.ForeignKey(Specialites,  on_delete=models.CASCADE, to_field='id',
                             related_name='agendas',
                            related_query_name='agenda', null=True)


    disponibilite=models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)




