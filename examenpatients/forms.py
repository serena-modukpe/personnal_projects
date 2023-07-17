from django import forms
from .models import Examenpatients
from django.forms import ModelForm

class ExamenpatientsForm(forms.ModelForm):
    class Meta:
        model = Examenpatients
        fields = ( "resultat",'description', 'type_examens', 'dossierpatients','users')
