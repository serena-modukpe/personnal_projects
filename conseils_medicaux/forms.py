from django import forms
from .models import Conseils_Medicaux

class ConseilsForm(forms.ModelForm):
    class Meta:
        model = Conseils_Medicaux
        fields = ("type","description")
