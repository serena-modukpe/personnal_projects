from django import forms
from .models import Habilitations


class HabilitationsForm(forms.ModelForm):
    class Meta:
        model = Habilitations
        fields = ("libelle", "description")