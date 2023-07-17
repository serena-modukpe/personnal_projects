
from django import forms
from .models import Rendezvous

class RendezvousForm(forms.ModelForm):
    class Meta:
        model = Rendezvous
        fields = ('specialites', 'agendas', 'users')

class RendezvousCreateForm(forms.ModelForm):
    class Meta:
        model = Rendezvous
        fields = ('specialites', 'agendas', 'users', 'statut')
     
  

    