from django.db import models


# Create your models here.
class Specialites(models.Model):
    libelle = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)

