from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from consultations.forms import ConsultationsForm
from consultations.models import Consultations
import datetime
import sweetify

# Create your views here.

def index(request):
  consultations = Consultations.objects.all()
  template = loader.get_template('backend/consultations/index.html')
  context = {
      'consultations':consultations,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  consultations = Consultations.objects.all()
  template = loader.get_template('backend/consultations/create.html')
  context = {
      'form': ConsultationsForm,
      'consultations': consultations,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  consultations = Consultations.objects.all()
  if request.method == "POST":
      form= ConsultationsForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            cout = form.cleaned_data.get('cout')
            created_at = datetime.datetime.now()
            consultations = Consultations.objects.create(
                libelle=libelle,
                description=description,
                cout=cout,
                created_at=created_at,
            )
            consultations.save()
            sweetify.success(request, 'consultation enregistrée avec succès', button='Fermer', timer=5000)
      else:
        sweetify.error(request, 'Cette consultation existe dejà', button='Fermer', timer=5000)
        return redirect('consultations.create')
  
  return HttpResponseRedirect(reverse("consultations.index"))

def edit(request, id):
  consultations = Consultations.objects.get(id=id)
  template = loader.get_template('backend/consultations/edit.html')
  context = {
      'consultations': consultations,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    consultations = Consultations.objects.get(id=id)
    if request.method == 'POST':
        form = ConsultationsForm(request.POST, request.FILES, instance=consultations)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            cout = form.cleaned_data.get('cout')
            consultations.libelle = libelle
            consultations.description = description
            consultations.cout = cout
            consultations.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'consultation mise à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("consultations.index"))
   

def delete(request, id):
    consultations = Consultations.objects.get(id=id)
    consultations.delete()
    sweetify.success(request, 'consultation supprimée', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("consultations.index"))
