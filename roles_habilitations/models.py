from django.db import models
from roles.models import Roles
from habilitations. models import Habilitations

class Users(models.Model):
    roles = models.ForeignKey(Roles,on_delete=models.CASCADE, to_field='id',
                             related_name='roles_habilitations',
                            related_query_name='role_habilitation', null=True)
    
    habilitations = models.ForeignKey(Habilitations,on_delete=models.CASCADE, to_field='id',
                             related_name='roles_habilitations',
                            related_query_name='role_habilitation', null=True)
    desrolhab = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    created_by = models.DateTimeField(auto_now_add=True, null=True)

    update_at = models.DateTimeField(auto_now_add=True, null=True)

    update_by = models.DateTimeField(auto_now_add=True, null=True)

    

