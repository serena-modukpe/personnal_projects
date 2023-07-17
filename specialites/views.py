from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from specialites.forms import SpecialitesForm
from specialites.models import Specialites
import datetime
import sweetify

# Create your views here.


# Create your views here.

def index(request):
  specialites = Specialites.objects.all()
  template = loader.get_template('backend/specialites/index.html')
  context = {
      'specialites':specialites,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  specialites = Specialites.objects.all()
  template = loader.get_template('backend/specialites/create.html')
  context = {
      'form': Specialites(),
      'specialites': specialites,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  specialites = Specialites.objects.all()
  if request.method == "POST":
      form= SpecialitesForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            updated_at = datetime.datetime.now()
            specialites = Specialites.objects.create(
                libelle=libelle,
                description=description,
                created_at=created_at,
                updated_at=updated_at,
            )
            specialites.save()
            sweetify.success(request, 'Spécialité enregistrée avec succès', button='Fermer', timer=5000)
      else:
        sweetify.error(request, 'Cette specialité existe déjà', button='Fermer', timer=5000)
        return redirect('specialites.create')
  
  return HttpResponseRedirect(reverse("specialites.index"))

def edit(request, id):
  specialites = Specialites.objects.get(id=id)
  template = loader.get_template('backend/specialites/edit.html')
  context = {
      'specialites': specialites,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    specialites = Specialites.objects.get(id=id)
    if request.method == 'POST':
        form = SpecialitesForm(request.POST, request.FILES, instance=specialites)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            specialites.libelle = libelle
            specialites.description = description
            specialites.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'Spécialité mise à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("specialites.index"))
   

def delete(request, id):
    specialites = Specialites.objects.get(id=id)
    specialites.delete()
    sweetify.success(request, 'Spécialité supprimée', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("specialites.index"))
