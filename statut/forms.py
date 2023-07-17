from django import forms
from .models import Statut


class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = ("libelle", "description")