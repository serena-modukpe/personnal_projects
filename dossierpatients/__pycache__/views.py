from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Prescriptions
from .forms import PrescriptionsForm
from .models import Personnes
from django.shortcuts import redirect

# Create your views here.

def index(request):
    prescriptions = Prescriptions.objects.select_related().all()
    personnes= Personnes.objects.all()
    template = loader.get_template('backend/prescriptions/index.html')
    context = {
        'prescriptions': prescriptions,
        'personnes':personnes,
       
    }
    return HttpResponse(template.render(context, request))



def create(request):
        prescriptions = Prescriptions.objects.select_related().all()
        personnes = Personnes.objects.all()

        template = loader.get_template('backend/prescriptions/create.html')
        context = {
            "form": PrescriptionsForm(),
            'personnes': personnes,
            'prescriptions':prescriptions,
            
        }
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = PrescriptionsForm(request.POST)
        if form.is_valid():
            quantite = form.cleaned_data.get('quantite')
            possologie= form.cleaned_data.get('possologie')
            medicament =form.cleaned_data.get('medicament')
            categorie_prescription =form.cleaned_data.get('categorie_prescription')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            personnes = form.cleaned_data.get('personnes')
            prescriptions = Prescriptions.objects.create (
                quantite  = quantite,
                possologie =possologie,
                medicament=medicament,
                categorie_prescription=categorie_prescription,
                created_at = created_at,
                updated_at = updated_at,
                personnes = personnes,
            )
            prescriptions.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('prescriptions.index'))

def edit(request, id):
    
        personnes = Personnes.objects.all()
        prescriptions= Prescriptions.objects.select_related().get(id=id)
        template = loader.get_template('backend/prescriptions/edit.html')
        context = {
            'prescriptions': prescriptions,
            'personnes': personnes,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    prescriptions = Prescriptions.objects.select_related().get(id=id)
    if request.method == "POST":
        quantite = request.POST['quantite']
        possologie= request.POST['possologie']
        medicament = request.POST['medicament']
        personnes = request.POST['personnes']
        form = PrescriptionsForm(request.POST, instance=prescriptions)
        if form.is_valid():
            prescriptions.quantite  = quantite
            prescriptions.possologie =possologie
            prescriptions.medicament=medicament
            prescriptions.personnes=Personnes.objects.get(id=personnes)
            prescriptions.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('prescriptions.index'))




def delete(request, id):
   prescriptions= Prescriptions.objects.get(id=id)
   prescriptions.delete()
   return HttpResponseRedirect(reverse('prescriptions.index'))


