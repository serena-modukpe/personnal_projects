from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Medecins
from .forms import MedecinsForm
from .models import Personnes
from .models import Specialites
from django.shortcuts import redirect
import sweetify

# Create your views here.

def index(request):
    medecins = Medecins.objects.select_related().all()
    personnes= Personnes.objects.select_related("users").filter(users__roles=2).all()
    specialites= Specialites.objects.all()
    template = loader.get_template('backend/medecins/index.html')
    context = {
        'medecins': medecins,
        'personnes':personnes,
        'specialites':specialites,
       
    }
    return HttpResponse(template.render(context, request))



def create(request):
        medecins = Medecins.objects.select_related().all()
        personnes= Personnes.objects.select_related("users").filter(users__roles=2).all()
        specialites = Specialites.objects.all()

        template = loader.get_template('backend/medecins/create.html')
        context = {
            "form": MedecinsForm(),
            'personnes': personnes,
            'specialites':specialites,
            'medecins':medecins,
            
        }
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = MedecinsForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            telephone = form.cleaned_data.get('telephone')
            email = form.cleaned_data.get('email')
            adresse = form.cleaned_data.get('adresse')
            telephone = form.cleaned_data.get('telephone')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            personnes = form.cleaned_data.get('personnes')
            specialites = form.cleaned_data.get('specialites')
            medecins = Medecins.objects.create (
                nom = nom,
                prenom = prenom,
                telephone = telephone,
                email = email,
                adresse = adresse,
                created_at = created_at,
                updated_at = updated_at,
                personnes = personnes,
                specialites= specialites,
            )
            medecins.save()
            sweetify.success(request, 'Medecin enregistré avec succès', button='Fermer', timer=5000)
        else:
            sweetify.error(request, 'Ce medecin existe dejà', button='Fermer', timer=5000)
            return redirect('medecins.create')
    return HttpResponseRedirect(reverse('medecins.index'))

def edit(request, id):
    
        personnes= Personnes.objects.select_related("users").filter(users__roles=2).all()
        specialites = Specialites.objects.all()
        medecins= Medecins.objects.select_related().get(id=id)
        template = loader.get_template('backend/medecins/edit.html')
        context = {
            'medecins': medecins,
            'personnes': personnes,
            'specialites': specialites,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    medecins = Medecins.objects.select_related().get(id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        prenom= request.POST['prenom']
        telephone = request.POST['telephone']
        email = request.POST['email']
        adresse = request.POST['adresse']
        personnes = request.POST['personnes']
        specialites = request.POST['specialites']
        form = MedecinsForm (request.POST, instance=medecins)
        if form.is_valid():
            medecins.nom  = nom
            medecins.prenom =prenom
            medecins.telephone=telephone
            medecins.email=email
            medecins.adresse=adresse
            medecins.personnes=Personnes.objects.get(id=personnes)
            medecins.specialites=Specialites.objects.get(id=specialites)
            medecins.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('medecins.index'))




def delete(request, id):
   medecins= Medecins.objects.get(id=id)
   medecins.delete()
   return HttpResponseRedirect(reverse('medecins.index'))


