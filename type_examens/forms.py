from django import forms
from .models import Type_examens


class  Type_examensForm(forms.ModelForm):
    class Meta:
        model = Type_examens
        fields =("libelle", "description")
    