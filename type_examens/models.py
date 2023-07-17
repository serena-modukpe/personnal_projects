from django.db import models

# Create your models here.
class Type_examens(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)