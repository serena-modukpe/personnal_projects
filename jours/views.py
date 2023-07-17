from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from jours.forms import JoursForm
from jours.models import Jours
import datetime
import sweetify


# Create your views here.

def index(request):
  jours = Jours.objects.all()
  template = loader.get_template('backend/jours/index.html')
  context = {
      'jours':jours,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  jours = Jours.objects.all()
  template = loader.get_template('backend/jours/create.html')
  context = {
      'form': Jours(),
      'jours': jours,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  jours = Jours.objects.all()
  if request.method == "POST":
      form= JoursForm(request.POST, request.FILES)
      if form.is_valid():
            date = form.cleaned_data.get('date')
            created_at = datetime.datetime.now()
            updated_at = datetime.datetime.now()
            jours = Jours.objects.create(
                date=date,
                created_at=created_at,
                updated_at=updated_at,
            )
            jours.save()
            sweetify.success(request, 'Jour enregistré avec succès', button='Fermer', timer=5000)
      else:
        sweetify.error(request, 'Cette date existe dejà', button='Fermer', timer=5000)
        return redirect('jours.create')
  
  return HttpResponseRedirect(reverse("jours.index"))

def edit(request, id):
  jours = Jours.objects.get(id=id)
  template = loader.get_template('backend/jours/edit.html')
  context = {
      'jours': jours,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    jours = Jours.objects.get(id=id)
    if request.method == 'POST':
        form = JoursForm(request.POST, request.FILES, instance=jours)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            jours.date = date
            jours.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'jour mis à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("jours.index"))
   

def delete(request, id):
    jours = Jours.objects.get(id=id)
    jours.delete()
    sweetify.success(request, 'jour supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("jours.index"))
