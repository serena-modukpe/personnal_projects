from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Prescriptions
from rendezvous.models import Rendezvous
from dossierpatients.models import Dossierpatients
from .forms import PrescriptionsForm
from authentication.models import Users
from django.shortcuts import redirect
import sweetify

# Create your views here.

def index(request, id, user_id, dossierpatients_id):
    
    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    prescriptions = Prescriptions.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
    dossierpatients= Dossierpatients.objects.get(id=dossierpatients_id)
    dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
    template = loader.get_template('backend/prescriptions/index.html')
    context = {
        'prescriptions': prescriptions,
        'dossierpatients':dossierpatients,
        'users':users,
        'patient':patient,
       
    }
    return HttpResponse(template.render(context, request))



def create(request, id ,user_id):
        users= Rendezvous.objects.select_related('users').get(id=id)
        patient = Users.objects.filter(id=user_id).latest('id')
        #get_users = Users.objects.select_related().filter(roles=1).all()
        prescriptions = Prescriptions.objects.select_related().all()
        dossierpatients = Dossierpatients.objects.select_related().filter(users=user_id)

        template = loader.get_template('backend/prescriptions/create.html')
        context = {
            "form": PrescriptionsForm(),
            'dossierpatients': dossierpatients,
            'prescriptions':prescriptions,
            'patient': patient,
            'users': users,
            #'get_users':get_users
            
        }
        return HttpResponse(template.render(context, request))
   
def store(request,id, user_id):
    users= Rendezvous.objects.select_related('users').get(id=id)
    #get_users = Users.objects.select_related().filter(roles=1).all()
    patient = Users.objects.filter(id=user_id).latest('id')
    if request.method == "POST":
        form = PrescriptionsForm(request.POST)
        if form.is_valid():
            quantite = form.cleaned_data.get('quantite')
            possologie= form.cleaned_data.get('possologie')
            medicament =form.cleaned_data.get('medicament')
            categorie_prescription =form.cleaned_data.get('categorie_prescription')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            dossierpatients = form.cleaned_data.get('dossierpatients')
            users = form.cleaned_data.get('users')
            prescriptions = Prescriptions.objects.create (
                quantite  = quantite,
                possologie =possologie,
                medicament=medicament,
                dossierpatients = dossierpatients,
                categorie_prescription=categorie_prescription,
                created_at = created_at,
                updated_at = updated_at,
                users= users
                
              
            )
            prescriptions.save()
            sweetify.success(request, 'Prescription enregistrée avec succès', button='Fermer', timer=5000)
            return redirect('prescriptions.index', id=id, user_id=user_id, dossierpatients_id=dossierpatients.id)
        else:
            sweetify.error(request, 'Cette prescription existe dejà', button='Fermer', timer=5000)
            return redirect('prescriptions.create')

def edit(request, id):
    
        dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
        prescriptions= Prescriptions.objects.select_related().get(id=id)
        template = loader.get_template('backend/prescriptions/edit.html')
        context = {
            'prescriptions': prescriptions,
            'dossierpatients': dossierpatients,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
    users= Users.objects.select_related().filter(roles=1).all()
    prescriptions = Prescriptions.objects.select_related().get(id=id)
    if request.method == "POST":
        quantite = request.POST['quantite']
        possologie= request.POST['possologie']
        medicament = request.POST['medicament']
        users = request.POST['users']
        dossierpatients = request.POST['dossierpatients']
        form = PrescriptionsForm(request.POST, instance=prescriptions)
        if form.is_valid():
            prescriptions.quantite  = quantite
            prescriptions.possologie =possologie
            prescriptions.medicament=medicament
            prescriptions.dossierpatients=Dossierpatients.objects.get(id=dossierpatients)
            prescriptions.users=users.objects.get(id=users)
            prescriptions.save()
        else:
            return HttpResponse(form.errors)
        sweetify.success(request, ' Prescription mise à jour avec succès', button='Fermer', timer=5000)
           
    return HttpResponseRedirect(reverse('prescriptions.index'))




def delete(request, id):
   prescriptions= Prescriptions.objects.get(id=id)
   prescriptions.delete()
   return HttpResponseRedirect(reverse('prescriptions.index'))




def patients(request, dossierpatients_id):
    if request.user.is_authenticated:
        current_user=request.user
        id=current_user.id
        #consultationpatients = Consultationpatients.objects.select_related().filter(dossierpatients=id).all()
        dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
        dossier= Dossierpatients.objects.get(id=dossierpatients_id)
        prescriptions = Prescriptions.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
        template = loader.get_template('backend/prescriptions/index_patient.html')
        context = {
            'prescriptions': prescriptions,
            'dossierpatients': dossierpatients,
            'dossier':dossier
            
        }

        return HttpResponse(template.render(context, request))
    else:
         return redirect('auth.login')








    



   

