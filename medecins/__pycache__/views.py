from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Dossierpatients
from .forms import DossierpatientsForm
from .models import Personnes
from django.shortcuts import redirect

# Create your views here.

def index(request):
    dossierpatients = Dossierpatients.objects.select_related().all()
    personnes= Personnes.objects.all()
    template = loader.get_template('backend/dossierpatients/index.html')
    context = {
        'dossierpatients': dossierpatients,
        'personnes':personnes,
       
    }
    return HttpResponse(template.render(context, request))



def create(request):
        dossierpatients = Dossierpatients.objects.select_related().all()
        personnes = Personnes.objects.all()

        template = loader.get_template('backend/dossierpatients/create.html')
        context = {
            "form": DossierpatientsForm(),
            'personnes': personnes,
            'dossierpatients':dossierpatients,
            
        }
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = DossierpatientsForm(request.POST)
        if form.is_valid():
            
            numero =form.cleaned_data.get('numero')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            personnes = form.cleaned_data.get('personnes')
            dossierpatients = Dossierpatients.objects.create (
                numero  = numero,
                created_at = created_at,
                updated_at = updated_at,
                personnes = personnes,
            )
            dossierpatients.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('dossierpatients.index'))

def edit(request, id):
    
        personnes = Personnes.objects.all()
        dossierpatients= Dossierpatients.objects.select_related().get(id=id)
        template = loader.get_template('backend/dossierpatients/edit.html')
        context = {
            'dossierpatients': dossierpatients,
            'personnes': personnes,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    dossierpatients = Dossierpatients.objects.select_related().get(id=id)
    if request.method == "POST":
        numero = request.POST['numero']
        personnes = request.POST['personnes']
        form = DossierpatientsForm(request.POST, instance=dossierpatients)
        if form.is_valid():
            
            dossierpatients.numero=numero
            dossierpatients.personnes=Personnes.objects.get(id=personnes)
            dossierpatients.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('dossierpatients.index'))




def delete(request, id):
   dossierpatients= Dossierpatients.objects.get(id=id)
   dossierpatients.delete()
   return HttpResponseRedirect(reverse('dossierpatients.index'))


