from django.db import models

# Create your models here.
class Consultations(models.Model):
    libelle = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)