from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from heures.forms import HeuresForm
from heures.models import Heures
import datetime
import sweetify


# Create your views here.

def index(request):
  heures = Heures.objects.all()
  template = loader.get_template('backend/heures/index.html')
  context = {
      'heures':heures,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  heures = Heures.objects.all()
  template = loader.get_template('backend/heures/create.html')
  context = {
      'form': HeuresForm(),
      'heures': heures,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  if request.method == "POST":
      form= HeuresForm(request.POST, request.FILES)
      if form.is_valid():
            heure = form.cleaned_data.get('heure')
            created_at = datetime.datetime.now()
            updated_at = datetime.datetime.now()
            heures = Heures.objects.create(
                heure=heure,
                created_at=created_at,
                updated_at=updated_at,
            )
            heures.save()
            sweetify.success(request, 'Heure enregistré avec succès', button='Fermer', timer=5000)
      else:
        
        return HttpResponse(form.errors)
  
  return HttpResponseRedirect(reverse("heures.index"))

def edit(request, id):
  heures = Heures.objects.get(id=id)
  template = loader.get_template('backend/heures/edit.html')
  context = {
      'heures': heures,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    heures = Heures.objects.get(id=id)
    if request.method == 'POST':
        form = HeuresForm(request.POST, request.FILES, instance=heures)
        if form.is_valid():
            heure = form.cleaned_data.get('heure')
            heures.heure = heure
            heures.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'heure mis à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("heures.index"))
   

def delete(request, id):
    heures = Heures.objects.get(id=id)
    heures.delete()
    sweetify.success(request, 'heure supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("heures.index"))