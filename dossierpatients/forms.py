from django import forms
from .models import Dossierpatients
from authentication.models import Users

class DossierpatientsForm(forms.ModelForm):
    class Meta:
        model = Dossierpatients
        fields = ( 'numero','users')



 