from django.db import models
from authentication.models import Users
# Create your models here.
class Dossierpatients(models.Model):
    
    numero = models.CharField(max_length=12, unique=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='id', related_name='dossierpatients', related_query_name='dossierpatient', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='dossier_created')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='dossier_updated')

def generate_numero(self):
    last_dossier = Dossierpatients.objects.order_by('-numero').first()
    if last_dossier:
        last_numero = int(last_dossier.numero[1:])
        new_numero = last_numero + 1
    else:
        new_numero = 1
    return 'D{:07d}'.format(new_numero)

def save(self, *args, **kwargs):
    if not self.numero:
        self.numero = self.generate_numero()
    super(Dossierpatients, self).save(*args, **kwargs)
