from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Roles

# Create your models here.
class Users(AbstractUser):
    adresse = models.CharField(max_length=255, null=True)
    ddn = models.DateField(null=True)
    telephone = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, to_field='id', related_name='users', related_query_name='user', null=True)

