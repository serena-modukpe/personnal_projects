from django import forms
from .models import Specialites


class SpecialitesForm(forms.ModelForm):
    class Meta:
        model = Specialites
        fields = ("libelle", "description")