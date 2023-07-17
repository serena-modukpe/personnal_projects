from django.db import models

# Create your models here.
class Heures(models.Model):
    heure = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)