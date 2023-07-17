from django import forms
from .models import Heures 
class HeuresForm(forms.ModelForm):
    class Meta:
        model = Heures
        fields = ("heure",)