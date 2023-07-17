from django import forms
from .models import Medecins
from django.forms import ModelForm, Textarea

class MedecinsForm(forms.ModelForm):
    class Meta:
        model = Medecins
        fields = ('nom','prenom','telephone','email','adresse',"specialites",'personnes')



 