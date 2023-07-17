from django.db import models

# Create your models here.
class Jours(models.Model):

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.TextField(null=True)