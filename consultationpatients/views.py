from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Consultationpatients
from .forms import ConsultationpatientsForm
from .models import Consultations
from .models import Dossierpatients
from prescriptions.models import Prescriptions
from examenpatients.models import Examenpatients
from authentication.models import Users
from rendezvous.models import Rendezvous
from django.shortcuts import redirect

import sweetify

# Create your views here.

def index(request, id, user_id, dossierpatients_id):
    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    consultations= Consultations.objects.all()
    dossierpatients= Dossierpatients.objects.get(id=dossierpatients_id)
    consultationpatients = Consultationpatients.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
    template = loader.get_template('backend/consultationpatients/index.html')
    context = {
        'users': users,
        'patient': patient,
        'consultationpatients': consultationpatients,
        'consultations':consultations,
        'dossierpatients':dossierpatients,
        
    }
    
    return HttpResponse(template.render(context, request))


def create(request, id, user_id):
    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    consultationpatients = Consultationpatients.objects.select_related('dossierpatients').filter(dossierpatients__users=id).all()
    consultations = Consultations.objects.all()
    dossierpatients = Dossierpatients.objects.select_related().filter(users=user_id)
    
    template = loader.get_template('backend/consultationpatients/create.html')
    context = {
        "form": ConsultationpatientsForm(),
        'consultations': consultations,
        'users': users,
        'patient': patient,
        'dossierpatients': dossierpatients,
        'consultationpatients': consultationpatients,
    }
    return HttpResponse(template.render(context, request))







def store(request, id ,user_id):

    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    dossierpatients = Dossierpatients.objects.select_related().get(users=user_id)
    if request.method == "POST":
        form = ConsultationpatientsForm(request.POST)
        if form.is_valid():
        
            observation =form.cleaned_data.get('observation')
            recommandation =form.cleaned_data.get('recommandation')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            consultations = form.cleaned_data.get('consultations')
            dossierpatients = form.cleaned_data.get('dossierpatients')
            
            consultationpatients = Consultationpatients.objects.create (
                observation = observation,
                created_at = created_at,
                updated_at = updated_at,
                consultations = consultations,
                dossierpatients = dossierpatients,
                recommandation = recommandation
            )
            consultationpatients.save()
            sweetify.success(request, 'Consultation prise avec succès', button='Fermer', timer=5000)
        return redirect('consultationpatients.index', id=id, user_id=user_id, dossierpatients_id=dossierpatients.id)
    else:
        #sweetify.error(request, 'Cette consultation existe déjà', button='Fermer', timer=5000)
        return redirect('consultationpatients.create', id=id, user_id=user_id)
  


def details(request, id):
    rendezvous = Rendezvous.objects.select_related('users').get(id=id)
    #dossierpatients = Dossierpatients.objects.get(users_id=rendezvous)
    consultationpatients = Consultationpatients.objects.select_related('dossierpatients').filter(dossierpatients__users=rendezvous.users).first()
    prescriptions = Prescriptions.objects.select_related('dossierpatients').filter(dossierpatients__users=rendezvous.users).first()
    examens = Examenpatients.objects.select_related('dossierpatients').filter(dossierpatients__users=rendezvous.users).first()
    template = loader.get_template('backend/consultationpatients/details.html')
    context = {
        #'dossierpatients':dossierpatients,
        #'users': users,
        'rendezvous': rendezvous,
      
        
        'consultationpatients': consultationpatients,
        'prescriptions': prescriptions,
        'examens':examens
    }
    return HttpResponse(template.render(context, request))




def edit(request, id):
    
        consultations = Consultations.objects.all()
        dossierpatients = Dossierpatients.objects.all()
        consultationpatients= Consultationpatients.objects.select_related().get(id=id)
        template = loader.get_template('backend/consultationpatients/edit.html')
        context = {
            'consultationpatients': consultationpatients,
            'consultation': consultations,
            'dossierpatients': dossierpatients,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    consultationpatients = Consultationpatients.objects.select_related().get(id=id)
    if request.method == "POST":
        observation = request.POST['observation']
        recommendation = request.POST['recommandation']
        consultations = request.POST['consultations']
        dossierpatients = request.POST['dossierpatients']
        form = ConsultationpatientsForm(request.POST, instance=consultationpatients)
        if form.is_valid():
            
            consultationpatients.observation=observation
            consultationpatients.recommandation=recommendation
            consultationpatients.consultations=Consultations.objects.get(id=consultations)
            consultationpatients.dossierpatients=Dossierpatients.objects.get(id=dossierpatients)
            consultationpatients.save()
        else:
            return HttpResponse(form.errors)
        sweetify.success(request, 'consultation patient mise à jour avec succès', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse('consultationpatients.index'))




def delete(request, id):
   consultationpatients= Consultationpatients.objects.get(id=id)
   consultationpatients.delete()
   sweetify.success(request, 'consultation patient supprimée avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('consultationpatients.index'))





def patients(request, dossierpatients_id):
    if request.user.is_authenticated:
        current_user=request.user
        id=current_user.id
        #consultationpatients = Consultationpatients.objects.select_related().filter(dossierpatients=id).all()
        dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
        dossier= Dossierpatients.objects.get(id=dossierpatients_id)
        consultationpatients = Consultationpatients.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
        template = loader.get_template('backend/consultationpatients/index_patient.html')
        context = {
            'consultationpatients': consultationpatients,
            'dossierpatients': dossierpatients,
            'dossier':dossier
            
        }

        return HttpResponse(template.render(context, request))
    else:
         return redirect('auth.login')


"""def consultation_patients(request, id, user_id):


    if request.user.is_authenticated:
        current_user=request.user
        id=current_user.id
        #consultationpatients = Consultationpatients.objects.select_related().filter(dossierpatients=id).all()
        #dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
        #rendezvous= Rendezvous.objects.select_related().get(id=id)
        users= Users.objects.select_related('rendezvous').filter(rendezvous__users=id).all()
        patient = Users.objects.filter(id=user_id).latest('id')
        consultationpatients = Consultationpatients.objects.select_related('dossierpatients').filter(dossierpatients__users=id).all()

        template = loader.get_template('backend/consultationpatients/consultation_patients.html')
        context = {
            'consultationpatients': consultationpatients,
            #'dossierpatients': dossierpatients,
            'patient':patient,
            #'rendezvous': rendezvous,
            'users': users
            
        }

        return HttpResponse(template.render(context, request))
    else:

        return redirect('auth.login')"""



 



