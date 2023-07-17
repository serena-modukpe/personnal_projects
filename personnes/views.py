from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Personnes
from .forms import PersonnesForm
from .models import Users
import sweetify


# Create your views here.

def index(request):
    personnes = Personnes.objects.select_related().all()
    users= Users.objects.select_related().all()
    template = loader.get_template('backend/personnes/index.html')
    context = {
        'personnes': personnes,
        'users':users,
       
    }
    
    return HttpResponse(template.render(context, request))



def create(request):
        personnes = Personnes.objects.select_related().all()
        users = Users.objects.all()
        template = loader.get_template('backend/personnes/create.html')
        context = {
            "form": PersonnesForm(),
            'personnes':personnes,
            'users': users,
            
        }
       

        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = PersonnesForm(request.POST)
        if form.is_valid():
            nom =form.cleaned_data.get('nom')
            prenoms =form.cleaned_data.get('prenoms')
            telephone =form.cleaned_data.get('telephone')
            ddn =form.cleaned_data.get('ddn')
            email =form.cleaned_data.get('email')
            adresse =form.cleaned_data.get('adresse')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            users = form.cleaned_data.get('users')
            personnes = Personnes.objects.create (
                nom = nom,
                prenoms = prenoms,
                telephone = telephone,
                ddn = ddn,
                email = email,
                adresse = adresse,
                created_at = created_at,
                updated_at = updated_at,
                users = users,
            )
            personnes.save()
            sweetify.success(request, ' Personne ajouté avec succès', button='Fermer', timer=5000)
            
        else:
            sweetify.error(request, 'Ce patient existe dejà', button='Fermer', timer=5000)
            return redirect('personnes.create')
       

    return HttpResponseRedirect(reverse('personnes.index'))

def edit(request, id):
        users = Users.objects.all()
        personnes= Personnes.objects.select_related().get(id=id)
        template = loader.get_template('backend/personnes/edit.html')
        context = {
            'personnes': personnes,
            'users': users,
        }
        return render(request, 'backend/personnes/edit.html', context)
    
        
def update(request, id):
    personnes = Personnes.objects.select_related().get(id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        prenoms = request.POST['prenoms']
        telephone = request.POST['telephone']
        ddn =  request.POST['ddn']
        email = request.POST['email']
        adresse = request.POST['adresse']
        users = request.POST['users']
        form = PersonnesForm(request.POST, instance=personnes)
        if form.is_valid():
            
            personnes.nom=nom
            personnes.prenoms=prenoms
            personnes.telephone=telephone
            personnes.ddn=ddn
            personnes.email=email
            personnes.adresse=adresse 
            personnes.users=Users.objects.get(id=users)
            personnes.save()
        else:
            return HttpResponse(form.errors)
        sweetify.success(request, ' Personnes mis à jour avec succès', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse('personnes.index'))




def delete(request, id):
   personnes= Personnes.objects.get(id=id)
   personnes.delete()
   sweetify.success(request, 'Personne supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('personnes.index'))
