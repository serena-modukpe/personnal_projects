from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Dossierpatients
from rendezvous.models import Rendezvous
from .forms import DossierpatientsForm
from authentication.models import Users
from django.shortcuts import redirect
import sweetify

from consultationpatients.models import Consultationpatients
from consultations.models import Consultations
from prescriptions.models import Prescriptions
from examenpatients.models import Examenpatients

# Create your views here.

def index(request):
    users= Users.objects.select_related().filter(roles=1).all()
    dossierpatients = Dossierpatients.objects.select_related().all()
    template = loader.get_template('backend/dossierpatients/index.html')
    context = {
        'dossierpatients': dossierpatients,
        'users':users,
       
    }
    return HttpResponse(template.render(context, request))






def consultation(request):
    consultationpatients = Consultationpatients.objects.select_related().all()
    dossierpatients = Dossierpatients.objects.all()
    template = loader.get_template('backend/dossierpatients/consultation.html')
    context = {
        'dossierpatients':dossierpatients,
        'consultationpatients':consultationpatients,
        
        
    }
    return HttpResponse(template.render(context, request))





def create(request):
        users= Users.objects.select_related().filter(roles=1).all()
        dossierpatients= Dossierpatients.objects.all()
        template = loader.get_template('backend/dossierpatients/create.html')
        context = {
            "form": DossierpatientsForm(),
            'users': users,
            'dossierpatients':dossierpatients,
            
        }
        
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = DossierpatientsForm(request.POST)
        if form.is_valid():
            #numero =form.cleaned_data.get('numero')
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            users = form.cleaned_data.get('users')
            dossierpatients = Dossierpatients.objects.create (
                #numero  = numero,
                created_at = created_at,
                updated_at = updated_at,
                users = users,
            )
            dossierpatients.save()
        else:
            return HttpResponse(form.errors)
           #sweetify.error(request, 'Les libellés existent déjà', button='Fermer', timer=5000)
    sweetify.success(request, 'Dossier enregistré avec succès', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("dossierpatients.index"))

def edit(request, id):    
    users= Users.objects.select_related().filter(roles=1).all()
    dossierpatients= Dossierpatients.objects.select_related().get(id=id)
    template = loader.get_template('backend/dossierpatients/edit.html')
    context = {
        'dossierpatients': dossierpatients,
        'users': users,
    }
    sweetify.success(request, 'dossier patient mis à jour avec succès', button='Fermer', timer=5000)
    return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    dossierpatients = Dossierpatients.objects.select_related().get(id=id)
    if request.method == "POST":
        #numero = request.POST['numero']
        users = request.POST['users']
        form = DossierpatientsForm(request.POST, instance=dossierpatients)
        if form.is_valid():
            
            #dossierpatients.numero=numero
            dossierpatients.users=users.objects.get(id=users)
            dossierpatients.save()
        else:
            return HttpResponse(form.errors)
        sweetify.success(request, 'dossier patient modifié avec succès', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse('dossierpatients.index'))




def delete(request, id):
   dossierpatients= Dossierpatients.objects.get(id=id)
   dossierpatients.delete()
   sweetify.success(request, 'dossier patient supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('dossierpatients.index'))


def creer_patient(request, id):
        # vérifier si le patient a déjà un dossier
        dossierpatients = Dossierpatients.objects.select_related().filter(users=id).first()
        if dossierpatients : 
            template = loader.get_template('backend/dossierpatients/dossierpatient.html')
            context = {
                'dossierpatients':dossierpatients,
                #'dossierpatients':dossierpatients,
                #'users': users,
                
            }
            return HttpResponse(template.render(context, request))
        else : 
            patient = Users.objects.get(id=id)
            # Aucun dossier n'existe, vous pouvez en créer un nouveau
            last_dossier = Dossierpatients.objects.order_by('-numero').first()
            if last_dossier:
                # récupérer le dernier numero
                last_numero = last_dossier.numero
                # convertir le numero en tableau pour extrait le code
                convert_num_tab = last_numero.split("-")
                # extrait le code qui se trouve à l'index 1 de notre tableau
                code_num = convert_num_tab[1]
                code_num = int(code_num)
                numero = code_num + 1
                code = "DOS"
                convert_num_format = str(numero).rjust(5,"0")
                code_dossier = code+'-'+convert_num_format

            else:
                #DOS-00001
                code = "DOS"
                numero = 1
                convert_num_format = str(numero).rjust(5,"0")
                code_dossier = code+'-'+convert_num_format

            #numero_new = 'D{:07d}'.format(numero)
            #récupérer l'identité du patien
           
            new_dossier = Dossierpatients.objects.create(
                numero=code_dossier,
                users=patient,
                created_by=request.user,
                updated_by=request.user
            )

            template = loader.get_template('backend/dossierpatients/dossierpatient.html')
            context = {
                'dossierpatients':new_dossier,
                #'dossierpatients':dossierpatients,
                #'users': users,
                
            }
            return HttpResponse(template.render(context, request))

           
        



def mes_dossier(request):
    current_user = request.user
    id = current_user.id
    dossierpatients = Dossierpatients.objects.select_related().filter(users=id).all()
    #dossier= Dossierpatients.objects.get(id=id)
    #rendezvous = Rendezvous.objects.select_related().all()
    template = loader.get_template('backend/dossierpatients/index_patient.html')
    context = {
        'dossierpatients':dossierpatients,
        #'dossier': dossier

    }
    return HttpResponse(template.render(context, request))


def dossier(request, id, user_id):
    users = Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')

    current_user = request.user

    # Vérifier si un dossier existe déjà pour ce patient
    dossier = Dossierpatients.objects.filter(users=patient).first()

    if dossier:
        # Un dossier existe déjà, vous pouvez l'afficher directement
       
        template = loader.get_template('backend/dossierpatients/dossier.html')
        context = {
            'users': users,
            'patient': patient,
            'dossierpatients': dossier
        }
        return HttpResponse(template.render(context, request))

    # Aucun dossier n'existe, vous pouvez en créer un nouveau
    last_dossier = Dossierpatients.objects.order_by('-numero').first()
    if last_dossier:
        #récupérer le dernier numero
        last_numero = last_dossier.numero
        # convertir le numero en tableau pour extrait le code
        convert_num_tab = last_numero.split("-")
        # extrait le code qui se trouve à l'index 1 de notre tableau
        code_num = convert_num_tab[1]
        code_num = int(code_num)
        numero = code_num + 1
        code = "DOS"
        convert_num_format = str(numero).rjust(5,"0")
        code_dossier = code+'-'+convert_num_format
    else:
        numero = 1
        #numero_new = 'DOS-{:05d}'.format(numero)
        code = "DOS"
        convert_num_format = str(numero).rjust(5,"0")
        code_dossier = code+'-'+convert_num_format

        new_dossier = Dossierpatients.objects.create(
            numero=code_dossier,
            users=patient,
            created_by=current_user,
            updated_by=current_user
        )

    template = loader.get_template('backend/dossierpatients/dossier.html')
    context = {
        'users': users,
        'patient': patient,
        'dossierpatients': new_dossier
    }
    return HttpResponse(template.render(context, request))

def liste_dossiers(request, id):
    # Récupérer l'utilisateur courant
    user = request.user

    # Utiliser l'utilisateur courant dans votre logique de traitement ici
    dossierpatients = Dossierpatients.objects.get(id=id)


    template = loader.get_template('backend/dossierpatients/liste_dossiers.html')
    context = {
        'dossierpatients': dossierpatients,
    }

    return HttpResponse(template.render(context, request))

