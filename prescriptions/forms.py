from django import forms
from .models import Prescriptions
from django.forms import ModelForm, Textarea

class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = ('quantite', 'possologie', 'medicament','users','categorie_prescription','dossierpatients')



 