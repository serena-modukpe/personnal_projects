from django import forms
from .models import Consultationpatients
from django.forms import ModelForm, Textarea

class ConsultationpatientsForm(forms.ModelForm):
    class Meta:
        model = Consultationpatients
        fields = ( "observation", 'recommandation', 'consultations', 'dossierpatients')



 