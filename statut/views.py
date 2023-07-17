from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from statut.forms import StatutForm
from statut.models import Statut
import datetime
import sweetify

# Create your views here.

def index(request):
  statut = Statut.objects.all()
  template = loader.get_template('backend/statut/index.html')
  context = {
      'statut':statut,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  statut = Statut.objects.all()
  template = loader.get_template('backend/statut/create.html')
  context = {
      'form': StatutForm,
      'statut': statut,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  statut = Statut.objects.all()
  if request.method == "POST":
      form= StatutForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            updated_at = datetime.datetime.now()
            statut = Statut.objects.create(
                libelle=libelle,
                description=description,
                created_at=created_at,
                updated_at=updated_at
            )
            statut.save()
            sweetify.success(request, 'statut enregistré avec succès', button='Fermer', timer=5000)
      else:
        sweetify.error(request, 'Ce statut existe dejà', button='Fermer', timer=5000)
        return redirect('statut.create')
  
  return HttpResponseRedirect(reverse("statut.index"))

def edit(request, id):
  statut = Statut.objects.get(id=id)
  template = loader.get_template('backend/statut/edit.html')
  context = {
      'statut': statut,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    statut = Statut.objects.get(id=id)
    if request.method == 'POST':
        form = StatutForm(request.POST, request.FILES, instance=statut)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            statut.libelle = libelle
            statut.description = description
            statut.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'statut mis à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("statut.index"))
   

def delete(request, id):
    statut = Statut.objects.get(id=id)
    statut.delete()
    sweetify.success(request, 'statut supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("statut.index"))
