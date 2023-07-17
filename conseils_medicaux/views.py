from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#from conseils_medicaux.forms import ConseilsForm
from conseils_medicaux.models import Conseils_Medicaux
import datetime
import sweetify
from .forms import ConseilsForm


# Create your views here.

def index(request):
  conseils_medicaux = Conseils_Medicaux.objects.all()
  template = loader.get_template('backend/conseils/index.html')
  context = {
      'conseils_medicaux':conseils_medicaux,
  }
  return HttpResponse(template.render(context, request))

def create(request):
  conseils_medicaux = Conseils_Medicaux.objects.all()
  template = loader.get_template('backend/conseils/create.html')
  context = {
      'form': ConseilsForm(),
      'conseils_medicaux': conseils_medicaux,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  conseils_medicaux = Conseils_Medicaux.objects.all()
  if request.method == "POST":
      form= ConseilsForm(request.POST, request.FILES)
      if form.is_valid():
            type = form.cleaned_data.get('type')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            conseils_medicaux = Conseils_Medicaux.objects.create(
                type=type,
                description=description,
                created_at=created_at,
            )
            conseils_medicaux.save()
            sweetify.success(request, 'conseil enregistré avec succès', button='Fermer', timer=5000)

      else:
        return HttpResponse(form.errors)
      sweetify.error(request, 'ce conseil existe dejà', button='Fermer', timer=5000)
      return redirect('conseils_medicaux.create')
  return HttpResponseRedirect(reverse("conseils_medicaux.index"))

def edit(request, id):

    conseils_medicaux = Conseils_Medicaux.objects.get(id=id)
    template = loader.get_template('backend/conseils/edit.html')
    context = {
        'conseils_medicaux': conseils_medicaux,
    }
    return HttpResponse(template.render(context, request))

def update(request, id):
    conseils_medicaux = Conseils_Medicaux.objects.get(id=id)
    if request.method == 'POST':
        form = ConseilsForm(request.POST, request.FILES, instance=conseils_medicaux)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            description = form.cleaned_data.get('description')
            conseils_medicaux.type = type
            conseils_medicaux.description = description
            conseils_medicaux.save()
           
        else:
          return HttpResponse(form.errors)

        sweetify.success(request, 'Conseil mis à jour avec succès', button='Fermer', timer=5000)

        return HttpResponseRedirect(reverse("conseils_medicaux.index"))
   

def delete(request, id):
    conseils_medicaux = Conseils_Medicaux.objects.get(id=id)
    conseils_medicaux.delete()
    sweetify.success(request, 'conseil supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("conseils_medicaux.index"))


# Create your views here.
