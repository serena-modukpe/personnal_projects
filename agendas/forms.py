from django import forms
from  .models import Agendas


class AgendasForm(forms.ModelForm):
    class Meta:
        model = Agendas
        fields = ("heures","jours", "users", "disponibilite","statut", "specialites")