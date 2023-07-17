from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Habilitations
from .forms import HabilitationsForm
import datetime
import sweetify


# Create your views here.

def index(request):
  habilitations = Habilitations.objects.all()
  template = loader.get_template('backend/habilitations/index.html')
  context = {
      'habilitations':habilitations,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  habilitations = Habilitations.objects.all()
  template = loader.get_template('backend/habilitations/create.html')
  context = {
      'form': Habilitations(),
      'habilitations': habilitations,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  habilitations = Habilitations.objects.all()
  if request.method == "POST":
      form= HabilitationsForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            habilitations = Habilitations.objects.create(
                libelle=libelle,
                description=description,
                created_at=created_at,
            )
            habilitations.save()
            sweetify.success( request,'Habilitation ajouté avec succès', button='Fermer', timer=5000) 
      else:
        sweetify.error(request, 'Cet hailitation existe dejà', button='Fermer', timer=5000)
        return redirect('habilitations.create')
  x
  return HttpResponseRedirect(reverse("habilitations.index"))


def edit(request, id):
  habilitations = Habilitations.objects.get(id=id)
  template = loader.get_template('backend/habilitations/edit.html')
  context = {
      'habilitations': habilitations,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    habilitations = Habilitations.objects.get(id=id)
    if request.method == 'POST':
        form = HabilitationsForm(request.POST, request.FILES, instance=habilitations)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            habilitations.libelle = libelle
            habilitations.description = description
            habilitations.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'habilitation mise à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("habilitations.index"))

def delete(request, id):
    habilitations = Habilitations.objects.get(id=id)
    habilitations.delete()
    sweetify.success(request, 'habilitation supprimée', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("habilitations.index"))
