from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import Type_examensForm
from .models import Type_examens
import datetime
import sweetify 

# Create your views here.



def index(request):
  type_examens = Type_examens.objects.all()
  template = loader.get_template('backend/type_examens/index.html')
  context = {
      'type_examens': type_examens,
  }
  return HttpResponse(template.render(context, request))


def create(request):
  type_examens = Type_examens.objects.all()
  template = loader.get_template('backend/type_examens/create.html')
  context = {
      'form': Type_examensForm(),
      'type_examens': type_examens,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  type_examens = Type_examens.objects.all()
  if request.method == "POST":
      form= Type_examensForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            type_examens = Type_examens.objects.create(
                libelle=libelle,
                description=description,
                created_at=created_at,
            )
            type_examens.save()
      else:
        sweetify.error(request, 'Veuillez remplir les champs', button='Fermer', timer=5000)
        return redirect('type_examens.index')
  sweetify.success(request, 'type examens enregistré avec succès', button='Fermer', timer=5000)
  return HttpResponseRedirect(reverse("type_examens.index"))
        

def edit(request, id):
  type_examens = Type_examens.objects.get(id=id)
  template = loader.get_template('backend/type_examens/edit.html')
  context = {
      'type_examens': type_examens,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    type_examens = Type_examens.objects.get(id=id)
    if request.method == 'POST':
        form = Type_examensForm(request.POST, request.FILES, instance=type_examens)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            type_examens.libelle = libelle
            type_examens.description = description
            type_examens.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'type examens mis à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("type_examens.index"))
    

def delete(request, id):
    type_examens = Type_examens.objects.get(id=id)
    type_examens.delete()
    sweetify.success(request, 'Type examens supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("type_examens.index"))
 




