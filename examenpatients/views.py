from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Examenpatients
from .forms import ExamenpatientsForm
from .models import Dossierpatients
from type_examens.models import Type_examens
from rendezvous.models import Rendezvous
from authentication.models import Users
from django.shortcuts import redirect
import sweetify

# Create your views here.

def index(request, id, user_id,dossierpatients_id):
    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    examenpatients = Examenpatients.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
    dossier= Dossierpatients.objects.get(id=dossierpatients_id)
    type_examens= Type_examens.objects.all()
    template = loader.get_template('backend/examenpatients/index.html')
    context = {
        'examenpatients': examenpatients,
        'dossier':dossier,
        'users':users,
        'patient':patient,
        'type_examens':type_examens,
       
    }
    return HttpResponse(template.render(context, request))



def create(request,id ,user_id):
        users= Rendezvous.objects.select_related('users').get(id=id)
        patient = Users.objects.filter(id=user_id).latest('id')
        examenpatients = Examenpatients.objects.select_related().all()
        dossierpatients = Dossierpatients.objects.select_related().filter(users=user_id)
        type_examens = Type_examens.objects.select_related().all()

        template = loader.get_template('backend/examenpatients/create.html')
        context = {
            "form": ExamenpatientsForm(),
            'dossierpatients': dossierpatients,
            'type_examens': type_examens,
            'examenpatients':examenpatients,
            'users':users,
            'patient' :patient
            
        }
        
        
        return HttpResponse(template.render(context, request))





      
   
def store(request,id ,user_id):
    users= Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    if request.method == "POST":
        form = ExamenpatientsForm(request.POST)
        if form.is_valid():
            
            description =form.cleaned_data.get('description')
            resultat =form.cleaned_data.get('resultat')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            dossierpatients = form.cleaned_data.get('dossierpatients')
            type_examens = form.cleaned_data.get('type_examens')
            users = form.cleaned_data.get('users')
            examenpatients = Examenpatients.objects.create (
                description  = description,
                resultat  = resultat,
                created_at = created_at,
                updated_at = updated_at,
                dossierpatients = dossierpatients,
                type_examens = type_examens,
                users = users,
            )
            examenpatients.save()
            sweetify.success( request,'examen patient ajouté avec succès', button='Fermer', timer=5000)
            return redirect('examenpatients.index', id=id, user_id=user_id, dossierpatients_id=dossierpatients.id) 
        else:
            sweetify.error( request,'Cet examen patient existe dejà', button='Fermer', timer=5000) 
            return redirect('examenpatients.create')
        
    

def edit(request, id):
    
        dossierpatients = Dossierpatients.objects.all()
        type_examens = Type_examens.objects.all()
        examenpatients= Examenpatients.objects.select_related().get(id=id)
        template = loader.get_template('backend/examenpatients/edit.html')
        context = {
            'examenpatients': examenpatients,
            'dossierpatients': dossierpatients,
            'type_examens': type_examens,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    examenpatients = Examenpatients.objects.select_related().get(id=id)
    if request.method == "POST":
        description = request.POST['description']
        resultat = request.POST['resultat']
        dossierpatients = request.POST['dossierpatients']
        type_examens = request.POST['type_examens']
        form = ExamenpatientsForm(request.POST, instance=examenpatients)
        if form.is_valid():
            examenpatients.resultat=resultat
            examenpatients.description=description
            examenpatients.dossierpatients=Dossierpatients.objects.get(id=dossierpatients)
            examenpatients.type_examens=Type_examens.objects.get(id=type_examens)
            examenpatients.save()
        else:
            return HttpResponse(form.errors)
    sweetify.success(request, 'examen patient modifié avec succès', button='Fermer', timer=5000)  
    return HttpResponseRedirect(reverse('examenpatients.index'))




def delete(request,id):
   examenpatients=Examenpatients.objects.get(id=id)
   examenpatients.delete()
   sweetify.success( request,'examen patient supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('examenpatients.index'))




def patients(request, dossierpatients_id):
    if request.user.is_authenticated:
        current_user=request.user
        id=current_user.id
        #consultationpatients = Consultationpatients.objects.select_related().filter(dossierpatients=id).all()
        dossierpatients= Dossierpatients.objects.select_related("users").filter(users__roles=1).all()
        dossier= Dossierpatients.objects.get(id=dossierpatients_id)
        examenpatients = Examenpatients.objects.select_related('dossierpatients').filter(dossierpatients=dossierpatients_id)
        template = loader.get_template('backend/examenpatients/index_patient.html')
        context = {
            'examenpatients': examenpatients,
            'dossierpatients': dossierpatients,
            'dossier':dossier
            
        }

        return HttpResponse(template.render(context, request))
    else:
         return redirect('auth.login')





         





