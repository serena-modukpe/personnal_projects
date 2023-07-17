from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Rendezvous
from .forms import RendezvousCreateForm
from .models import Users
from .models import Specialites
from .models import Statut
from .models import Agendas
import datetime
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
import six
from django.views.generic import View
from authentication.models import Users
from django.shortcuts import redirect
from prescriptions.models import Prescriptions
import sweetify







# Create your views here.

def index(request):
    rendezvous = Rendezvous.objects.select_related().all()
    users= Users.objects.select_related().filter(roles=1).all()
    specialites= Specialites.objects.all()
    agendas= Agendas.objects.all()
    statuts= Statut.objects.all()
    template = loader.get_template('backend/rendezvous/index.html')
    context = {
        'rendezvous': rendezvous,
        'users':users,
        'specialites':specialites,
        'agendas':agendas,
        'statuts':statuts,
       
    }
    return HttpResponse(template.render(context, request))


def create(request):
        rendezvous = Rendezvous.objects.select_related().all()
        users= Users.objects.select_related().filter(roles=1).all()
        specialites = Specialites.objects.all()
        agendas = Agendas.objects.all()
        statut = Statut.objects.all()

        template = loader.get_template('backend/rendezvous/create.html')
        context = {
            "form": RendezvousCreateForm(),
            'users': users,
            'specialites':specialites,
            'rendezvous':rendezvous,
            'statut':statut,
            'agendas':agendas,
            
        }
       
        return HttpResponse(template.render(context, request))

   
def store(request):
    if request.method == "POST":
        form = RendezvousCreateForm(request.POST)
        if form.is_valid():
            
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            users = form.cleaned_data.get('users')
            specialites = form.cleaned_data.get('specialites')
            statut = form.cleaned_data.get('statut')
            agendas = form.cleaned_data.get('agendas')
            rendezvous = Rendezvous.objects.create (
                created_at = created_at,
                updated_at = updated_at,
                users = users,
                specialites= specialites,
                statut= statut,
                agendas= agendas,
            )
            rendezvous.save()
        else:
            return HttpResponse(form.errors)
    sweetify.success (request,'rendez vous ajouté avec succès', button='Fermer', timer=5000)    
    return HttpResponseRedirect(reverse('rendezvous.index'))

def edit(request, id):
    if request.user.is_authenticated:
        users = Users.objects.select_related().filter(roles=1).all()
        specialites = Specialites.objects.all()
        statut = Statut.objects.all()
        agendas = Agendas.objects.all()
        rendezvous= Rendezvous.objects.select_related().get(id=id)
        template = loader.get_template('backend/rendezvous/edit.html')
        context = {
            'rendezvous': rendezvous,
            'users': users,
            'specialites': specialites,
            'statut': statut,
            'agendas': agendas,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('auth.login')
    
        
def update(request, id):
    rendezvous = Rendezvous.objects.select_related().get(id=id)
    if request.method == "POST":
        specialites = request.POST['specialites']
        users = request.POST['users']
        statut = request.POST['statut']
        agendas = request.POST['agendas']
        form = RendezvousCreateForm(request.POST, instance=rendezvous)
        if form.is_valid():
            users_obj = Users.objects.get(id=users)
            rendezvous.users = users_obj
            rendezvous.specialites = Specialites.objects.get(id=specialites)
            rendezvous.statut = Statut.objects.get(id=statut)
            rendezvous.agendas = Agendas.objects.get(id=agendas)
            rendezvous.save()

            if request.POST['statut'] == "1":  # Vérifiez si le statut est devenu "actif"
                # Envoyer un e-mail de confirmation à l'utilisateur
                subject = 'PRISE DE RENDEZ-VOUS'
                url_site = get_current_site(request)
                #text_body = render_to_string("mail_templates/message_body.txt", merge_data)
                html_body = render_to_string("email/email_rendezvous.html", {'statut':statut, 'users': users, 'agendas': agendas, 'specialites': specialites, 'url_site': url_site, 'rendezvous':rendezvous })
                msg = EmailMultiAlternatives(subject=subject, from_email="renaud@digiweb.bj",
                                            to=[users_obj.email], body=html_body)
                msg.attach_alternative(html_body, "text/html")
                msg.send()
                sweetify.success(request, 'Rendez-vous confirmé avec succès', button='Fermer', timer=5000)

        template = loader.get_template('backend/rendezvous/index.html')

        context = {
        }
        return HttpResponse(template.render(context, request))

    return HttpResponseRedirect(reverse("rendezvous.index"))

def delete(request, id):
   rendezvous= Rendezvous.objects.get(id=id)
   rendezvous.delete()
   sweetify.success(request,'rendez vous supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('rendezvous.index'))



"""
def appointment(request):
    users=Users.objects.all(),
    agendas=Agendas.objects.all(),
    statut=Statut.objects.all(),
    specialites=Specialites.objects.all(),

    template = loader.get_template('frontend/appointment.html')

    context = {
            "form": RendezvousForm(),
            'users': users,
            'specialites':specialites,
            'statut':statut,
            'agendas':agendas,
            
        }
    return HttpResponse(template.render(context, request))
    

def appointment_store(request):
    if request.method == "POST":
        form = RendezvousForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data.get('users')
            specialites = form.cleaned_data.get('specialites')
            statuts = form.cleaned_data.get('statuts')
            agendas = form.cleaned_data.get('agendas')
            rendezvous = Rendezvous.objects.create (
                users = users,
                specialites= specialites,
                statuts= statuts,
                agendas= agendas,
             )
            rendezvous.save()
        else:
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('frontend/appointment.html'))
"""



def patients(request):
   
    rendezvous= Rendezvous.objects.select_related().filter(statut=1).all()
    users = request.user
    #users= Users.objects.select_related().filter(roles=1).all()
    agendas= Agendas.objects.all()
    statut = Statut.objects.all()
    template = loader.get_template('backend/rendezvous/index_patient.html')
    context = {
        'rendezvous': rendezvous,
        'users':users,
        'agendas':agendas,
        'statut' : statut
    
    }
    return HttpResponse(template.render(context, request))

    #return redirect("auth.login")

def details(request):
    if request.user.is_authenticated:
        current_user= request.user
        id=current_user.id
        prescriptions = Prescriptions.objects.select_related(users=id).order_by('-id')
        users= Users.objects.select_related().filter(roles=1).all()
        agendas= Agendas.objects.all()
        statut = Statut.objects.all()
        template = loader.get_template('backend/rendezvous/details.html')
        context = {
            'prescriptions': prescriptions,
            'users':users,
            'agendas':agendas,
            'statut' : statut
        
        }
        return HttpResponse(template.render(context, request))


def liste_rendezvous(request):
    if request.user.is_authenticated:
        current_user= request.user
        id=current_user.id
        rendezvous= Rendezvous.objects.select_related('agendas').filter(agendas__users=id).all()
        users= Users.objects.select_related().filter(roles=1).all()
        agendas= Agendas.objects.all()
        statut = Statut.objects.all()
        template = loader.get_template('backend/rendezvous/liste_rendezvous.html')
        context = {
            'rendezvous': rendezvous,
            'users':users,
            'agendas':agendas,
            'statut' : statut
        
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("auth.login")
   
def mes_patients(request):
    if request.user.is_authenticated:
        current_user= request.user
        id=current_user.id
        rendezvous= Rendezvous.objects.select_related('agendas').filter(agendas__users=id).all()
        users= Users.objects.select_related().filter(roles=2).all()
        agendas= Agendas.objects.all()
        statut = Statut.objects.all()
        template = loader.get_template('backend/rendezvous/index_medecin.html')
        context = {
            'rendezvous': rendezvous,
            'users':users,
            'agendas':agendas,
            'statut' : statut
        
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("auth.login")
    


def ancien_rendezvous(request):
    if request.user.is_authenticated:
  
        current_user=request.user
        id=current_user.id
        rendezvous = Rendezvous.objects.select_related().filter(statut=2).all()
        specialites= Specialites.objects.all()
        agendas= Agendas.objects.all()
        statuts= Statut.objects.all()
        template = loader.get_template('backend/rendezvous/ancien_rendez_vous.html')
        context = {
            'rendezvous': rendezvous,
            'specialites':specialites,
            'agendas':agendas,
            'statuts':statuts,
        
        }
        return HttpResponse(template.render(context, request))
    else :
        return redirect('auth.login')


def changer_statut(request, id , user_id):
    #rendezvous = Rendezvous.objects.all()
    rendezvous= Rendezvous.objects.select_related('users').get(id=id)
    patient = Users.objects.filter(id=user_id).latest('id')
    specialites= Specialites.objects.all()
    agendas= Agendas.objects.all()
    statuts= Statut.objects.all()
    template = loader.get_template('backend/rendezvous/changer_statut.html')
    context = {
        'rendezvous': rendezvous,
        #'users':users,
        'specialites':specialites,
        'agendas':agendas,
        'statuts':statuts,
        'patient': patient
       
    }
    return HttpResponse(template.render(context, request))

"""def edit_changer_statut(request, id):
    if request.user.is_authenticated:
        users = Users.objects.select_related().filter(roles=1).all()
        specialites = Specialites.objects.all()
        statut = Statut.objects.all()
        agendas = Agendas.objects.all()
        rendezvous= Rendezvous.objects.select_related().get(id=id)
        template = loader.get_template('backend/rendezvous/changer_statut.html')
        context = {
            'rendezvous': rendezvous,
            'users': users,
            'specialites': specialites,
            'statut': statut,
            'agendas': agendas,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('auth.login')"""

def edit_changer_statut(request, id):
    rendezvous = Rendezvous.objects.select_related().get(id=id)
    
    rendezvous.statut = Statut.objects.get(id=2)
    rendezvous.save()
        
    return HttpResponseRedirect(reverse('rendezvous.liste_rendezvous'))


          