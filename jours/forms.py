from django import forms
from .models import Jours


class JoursForm(forms.ModelForm):
    class Meta:
        model = Jours
        fields = ("date",)
