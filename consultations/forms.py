from django import forms
from .models import Consultations


class ConsultationsForm(forms.ModelForm):
    class Meta:
        model = Consultations
        fields = ("libelle", "description", "cout")