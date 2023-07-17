from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import AgendasForm
from .models import Agendas
from .models import Jours
from .models import Heures
from authentication.models import Users
from statut.models import Statut
from specialites.models import Specialites

import sweetify


# Create your views here.

def index(request):
    agendas = Agendas.objects.select_related().all()
    jours= Jours.objects.all()
    heures= Heures.objects.all()
    statut= Statut.objects.all()
    users= Users.objects.select_related().filter(roles=2).all()
    specialites= Specialites.objects.all()
    template = loader.get_template('backend/agendas/index.html')
    context = {
        'agendas': agendas,
        'jours':jours,
        'heures':heures,
        'users':users,
        'statut': statut,
        'specialites': specialites
       
    }
    return HttpResponse(template.render(context, request))



def create(request):
        users= Users.objects.select_related().filter(roles=2).all()
        heures=Heures.objects.all()      
        agendas = Agendas.objects.select_related().all()
        jours = Jours.objects.all()
        statut= Statut.objects.all()
        specialites= Specialites.objects.all()
        template = loader.get_template('backend/agendas/create.html')
        context = {
            "form": AgendasForm(),
            'jours': jours,
            'users': users,
            'agendas':agendas, 
            'heures':heures,
            'statut':statut,
            'specialites': specialites
           
        }
        
          
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = AgendasForm(request.POST)
        if form.is_valid():
            
            disponibilite =form.cleaned_data.get('disponibilite')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            jours = form.cleaned_data.get('jours')
            heures = form.cleaned_data.get('heures')
            statut = form.cleaned_data.get('statut')
            users = form.cleaned_data.get('users')
            specialites = form.cleaned_data.get('specialites')
            agendas = Agendas.objects.create (
                disponibilite  = disponibilite,
                created_at = created_at,
                updated_at = updated_at,
                jours = jours,
                heures = heures,
                users = users,
                statut = statut,
                specialites = specialites,
            )
            agendas.save()
            
        else:
            return HttpResponse(form.errors)
    sweetify.success(request, 'agenda ajouté avec succès', button='Fermer', timer=5000)
        
    return HttpResponseRedirect(reverse('agendas.index'))

def edit(request, id):
    
        jours = Jours.objects.all()
        heures = Heures.objects.all()
        users= Users.objects.select_related().filter(roles=2).all()
        agendas= Agendas.objects.select_related().get(id=id)
        specialites = Specialites.objects.all()
        statut= Statut.objects.all()
        template = loader.get_template('backend/agendas/edit.html')
        context = {
            'agendas': agendas,
            'jours': jours,
            'heures': heures,
            'users': users,
            'statut':statut,
            'specialites':specialites
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    agendas = Agendas.objects.select_related().get(id=id)
    if request.method == "POST":
        disponibilite = request.POST['disponibilite']
        jours = request.POST['jours']
        heures = request.POST['heures']
        users = request.POST['users']
        statut = request.POST['satut']
        specialites = request.POST['specialites']
        form = AgendasForm(request.POST, instance=agendas)
        if form.is_valid():
            agendas.disponibilite=disponibilite
            agendas.jours=Jours.objects.get(id=jours)
            agendas.heures=Heures.objects.get(id=heures)
            agendas.users=Users.objects.get(id=users)
            agendas.statut=Statut.objects.get(id=statut)
            agendas.specialites=Specialites.objects.get(id=specialites)
            agendas.save()
        else:
            return HttpResponse(form.errors)
    sweetify.success(request, 'agenda modifié avec succès', button='Fermer', timer=5000)  
    return HttpResponseRedirect(reverse('agendas.index'))




def delete(request,id):
   agendas=Agendas.objects.get(id=id)
   agendas.delete()
   sweetify.success( request,'agenda supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('agendas.index'))


