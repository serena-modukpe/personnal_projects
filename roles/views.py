from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .forms import RolesForm
from authentication.models import Users

from .models import Roles
import datetime
import sweetify 
import six
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site


from rendezvous.models import Rendezvous
from rendezvous.forms import RendezvousForm
from personnes.models import Personnes
from specialites.models import Specialites
from statut.models import Statut
from agendas.models import Agendas
from authentication.models import Users
from django.http import JsonResponse

# Create your views here.

def accueil(request):
    template = loader.get_template('frontend/accueil.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('frontend/about.html')
    return HttpResponse(template.render())

def service(request):
  template = loader.get_template('frontend/service.html')
  return HttpResponse(template.render()) 


def rendezvous(request):
    if request.user.is_authenticated:
      #personnes=Personnes.objects.select_related("users").filter(users__roles=1).all()
      agendas=Agendas.objects.filter()
      statut=Statut.objects.all()
      specialites=Specialites.objects.all()

      template = loader.get_template('frontend/appointment.html')

      context = {
              'form': RendezvousForm(),
              'specialites':specialites,
              'statut':statut,
              'agendas':agendas,
              
          }
      return HttpResponse(template.render(context, request))
    else:
       return redirect('auth.login')




def rendezvous_store(request):
  if request.user.is_authenticated:
    if request.method == "POST":
        form = RendezvousForm(request.POST)
       
        if form.is_valid():
           
            users = form.cleaned_data.get('users')
            agendas = form.cleaned_data.get('agendas')
            specialites = form.cleaned_data.get('specialites')
            statut = Statut.objects.get(id=1)
            rendezvous = Rendezvous.objects.create(
                users=users,
                agendas=agendas,
                statut=statut,
                specialites=specialites,
            )
            statut_inactif = Statut.objects.get(libelle='INACTIF')
            agendas.statut = statut_inactif
            agendas.save()
           
            rendezvous.save()
             

           
               
            #Envoyer une notification à l'utilisateur
            message = 'Votre rendez-vous en ligne a été confirmé. Veuillez consulter votre boîte de réception pour trouver les détails de votre rendez-vous . Cordialement,[Sante-plus].'
            sweetify.info(request, message, button='Ok', timer=20000)

            #Envoyer un e-mail de confirmation à l'utilisateur
            subject = 'PRISE DE RENDEZ-VOUS'
            url_site = get_current_site(request)
            #text_body = render_to_string("mail_templates/message_body.txt", merge_data)
            html_body = render_to_string("email/email_rendezvous.html", {'statut':statut, 'users': users, 'agendas': agendas, 'specialites': specialites, 'url_site': url_site, 'rendezvous':rendezvous })
            msg = EmailMultiAlternatives(subject=subject, from_email="infosanteplus06@gmail.com",
                                        to=[users.email], body=html_body)
            msg.attach_alternative(html_body, "text/html")
            msg.send()


          
        else:
           return HttpResponse(form.errors)


            
        template = loader.get_template('frontend/accueil.html')

        context = {
        }
        return HttpResponse(template.render(context, request))
    
  else:
      return redirect('auth.login')     





def team(request):
  template = loader.get_template('frontend/team.html')
  return HttpResponse(template.render())

def temoignage(request):
  template = loader.get_template('frontend/testimonial.html')
  return HttpResponse(template.render())  

def contact(request):
  template = loader.get_template('frontend/contact.html')
  return HttpResponse(template.render())

def prix(request):
  template = loader.get_template('frontend/price.html')
  return HttpResponse(template.render())
"""
def signup(request):
 template = loader.get_template('frontend/connexion.html')
 return render(request,'frontend/signup.html')"""

def connexion(request):
  template = loader.get_template('frontend/connexion.html')
  return HttpResponse(template.render())

def dashbord(request):
  if request.user.is_authenticated:
    users = Users.objects.all().count()
    medecins = Users.objects.filter(roles=2).all().count()
    patients = Users.objects.filter(roles=1).all().count()
   
    template = loader.get_template('backend/dashbord.html')
    context = {
       'users': users,
       'patients':patients,
       'medecins': medecins,
       
    }
    return HttpResponse(template.render(context, request))
  else :
    return redirect('auth.login')

def dashbord_patient(request):
  if request.user.is_authenticated:
        patient = Users.objects.all()
        patient = request.user  # Supposons que vous ayez une relation entre l'utilisateur authentifié et le modèle Patient
        patient_id = patient.id 
        rendezvous_en_cours = Rendezvous.objects.select_related('').filter(users=patient_id, statut=1).count()
        
        template = loader.get_template('backend/dashbordpatient.html')
        context = {
            'rendezvous_en_cours': rendezvous_en_cours,
           
            'patient': patient
        }
        return HttpResponse(template.render(context, request))
  else:
        return redirect('auth.login')
  
def dashboard_medecin(request):
  if request.user.is_authenticated:
      
      medecin = request.user
      medecin_id = medecin.id
      rendezvous_en_cours= Rendezvous.objects.select_related('agendas').filter(agendas__users=medecin_id).count()
      #rendezvous_en_cours = Rendezvous.objects.select_related('').filter(users=medecin_id, statut=2).count()
      
      context = {
        
       'rendezvous_en_cours': rendezvous_en_cours,
             }
      template = loader.get_template('backend/dashboard_medecin.html')
      return HttpResponse(template.render(context, request))
  else :
      return redirect('auth.login')

def index(request):
  roles = Roles.objects.all()
  template = loader.get_template('backend/roles/index.html')
  context = {
      'roles': roles,
  }
  return HttpResponse(template.render(context, request))


def create(request):
  roles = Roles.objects.all()
  template = loader.get_template('backend/roles/create.html')
  context = {
      'form': RolesForm(),
      'roles': roles,
  }
  return HttpResponse(template.render(context, request))

def store(request):
  roles = Roles.objects.all()
  if request.method == "POST":
      form= RolesForm(request.POST, request.FILES)
      if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            created_at = datetime.datetime.now()
            roles = Roles.objects.create(
                libelle=libelle,
                description=description,
                created_at=created_at,
            )
            roles.save()
      else:
        sweetify.error(request, 'Veuillez remplir les champs', button='Fermer', timer=5000)
        return redirect('roles.index')
  sweetify.success(request, 'Rôle enregistré avec succès', button='Fermer', timer=5000)
  return HttpResponseRedirect(reverse("roles.index"))
        

def edit(request, id):
  roles = Roles.objects.get(id=id)
  template = loader.get_template('backend/roles/edit.html')
  context = {
      'roles': roles,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
    roles = Roles.objects.get(id=id)
    if request.method == 'POST':
        form = RolesForm(request.POST, request.FILES, instance=roles)
        if form.is_valid():
            libelle = form.cleaned_data.get('libelle')
            description = form.cleaned_data.get('description')
            roles.libelle = libelle
            roles.description = description
            roles.save()
           
        else:
          return HttpResponse(form.errors)

    sweetify.success(request, 'Rôle mis à jour avec succès', button='Fermer', timer=5000)

    return HttpResponseRedirect(reverse("roles.index"))
    

def delete(request, id):
    roles = Roles.objects.get(id=id)
    roles.delete()
    sweetify.success(request, 'Rôle supprimé', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse("roles.index"))
 




