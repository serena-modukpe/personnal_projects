from django import forms
from .models import Personnes


class  PersonnesForm(forms.ModelForm):
    class Meta:
        model = Personnes
        fields =("nom", "prenoms","telephone","ddn", "email", "adresse","users")
    