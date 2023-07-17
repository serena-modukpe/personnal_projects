from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login, logout # import des fonctions login et authenticate
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import  SignupForm, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import datetime
from .models import Users, Roles
from django.contrib.auth import views as auth_views
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError
import six
from . import views
from django.views.generic import View
import sweetify
from .forms import UsersForm, EditUsersForm
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from medecins.models import Medecins
from personnes.models import Personnes
from django.db.models import Q

# Create your views here.

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name= 'frontend/auth/login.html'
############# SIGN UP METHOD ####################

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            telephone = form.cleaned_data.get("telephone")
            adresse = form.cleaned_data.get("adresse")
            ddn = form.cleaned_data.get("ddn")
            created_at = datetime.datetime.now()
            roles = Roles.objects.get(id=1)
            password = make_password(form.cleaned_data.get("password1"))
            is_active = False
            

            #Passer les variables au modèle sous forme de tableau
            
            users = Users(first_name=first_name, last_name=last_name, email=email, telephone=telephone, password=password, adresse=adresse,ddn=ddn, username= email,is_active=is_active, roles=roles, created_at=created_at)
            users.save()

            personnes_id = Users.objects.filter(email=request.POST['email']).last()
            id = personnes_id.id
            personnes = Personnes.objects.create(users_id=id, telephone=telephone, adresse=adresse, nom=last_name, prenoms=first_name, email=email, ddn=ddn)
            personnes.save()

            #recupérer l'url courant du site
            url_du_site = get_current_site(request)
            #recpérer le domaine du site
            domain_web = url_du_site.domain
            #préparation dans une variable tableau des paramtres à passer aux templates d'envoie de mail
            account_activation_token = six.text_type(users.pk)+ six.text_type(created_at) + six.text_type(users.is_active)
            #token = make_token(auth)
            uid = urlsafe_base64_encode(force_bytes(users.pk))
            merge_data = {
                'first_name': first_name, 'last_name' : last_name, 'email' : email, 'url': domain_web, 'uid':uid
            }
            #envoie de mail à l'utilisateur nouvellement inscrit
            subject = "Santé PLUS : CREATION DE COMPTE"
            html_body = render_to_string("email/email_new_compte.html", merge_data)

            msg = EmailMultiAlternatives(subject=subject, from_email="infosanteplus06@gmail.com",to=[email])
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            
            #Notification de mail de l'inscription de l'utilisateur
            subject_notification = "Santé PLUS : CREATION DE COMPTE"
            html_body_notification = render_to_string("email/email_new_compte_notification.html", merge_data)

            msg = EmailMultiAlternatives(subject=subject_notification, from_email="infosanteplus06@gmail.com",to=["jenniferadelakoun9@gmail.com"])
            msg.attach_alternative(html_body_notification, "text/html")
            msg.send()
            #sweetify.success(request, 'Félicitations', text='Votre compte a été activé avec succès', persistent='ok')
            sweetify.success(request, 'Enregistrement effectuée avec succès. Veuillez vérifier votre mail.')
            return redirect('auth.login')
        else:
            messages.error(request, 'Inscription échouée.')
            return HttpResponse(form.errors)

    roles = Roles.objects.all()   
    template = loader.get_template('frontend/auth/signup.html')
    context = {
        'form': SignupForm(),
        'roles': roles,
        'current_host': request.get_host(),
    }
    #current_host = request.get_host()
    #sweetify.success(request, title='félicitations votre compte a été créé avec succès', button='OK', timer=5000)
    return HttpResponse(template.render(context, request))
   

    #return HttpResponse(current_host)
        
def activate(request, uidb64):
    Users = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        users = Users.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Users.DoesNotExist):
        users = None

    if users is not None:
        users.is_active = True
        users.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('auth.login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('auth.signup')



############# END SIGN UP METHOD ####################

########### LOGIN METHOD ##################
def customLogin(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            #return HttpResponse(user.roles)
            if user is not None:
                login(request, user)
                #return HttpResponse(user.roles.libelle)
                if request.user.roles.libelle == 'Patient':
                    #sweetify.success(request, 'Connexion réussie')
                    return redirect('accueil')
                elif user.roles.libelle == 'Médecin':
                        #sweetify.success(request, 'Connexion réussie')
                        return redirect('dashboard_medecin')
                else:
                    #sweetify.success(request, 'Connexion réussie')
                    return redirect('dashbord')
        else:
            messages.error(request, "Email ou de passe incorrect")
            return redirect("auth.login")
    else:
        return render(request, 'auth/login.html')
############## END LOGIN METHOD ####################


def userLogout(request):
    logout(request)
    #sweetify.success(request, title='Vous êtes déconnecté', button='OK', timer=5000)
    return redirect('accueil')


######################################### CRUD POUR USERS ######################################################################

def index(request):
    users = Users.objects.select_related().all()
    roles= Roles.objects.all()
    template = loader.get_template('backend/users/index.html')
    context = {
        'users': users,
        'roles':roles,
       
    }
    
    return HttpResponse(template.render(context, request))



def create(request):
        users = Users.objects.select_related().all()
        roles = Roles.objects.exclude(id=1).all()
        template = loader.get_template('backend/users/create.html')
        context = {
            "form": UsersForm(),
            'users': users,
            'roles':roles,
        }
       
        return HttpResponse(template.render(context, request))
   
def store(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            
            last_name =form.cleaned_data.get('last_name')
            first_name =form.cleaned_data.get('first_name')
            email =form.cleaned_data.get('email')
            telephone =form.cleaned_data.get('telephone')
            adresse =form.cleaned_data.get('adresse')
            password = make_password(form.cleaned_data.get("password"))
            created_at = form.cleaned_data.get('created_at')
            updated_at = form.cleaned_data.get('updated_at')
            roles = form.cleaned_data.get('roles')
            users = Users.objects.create (
                last_name = last_name,
                first_name = first_name,
                email = email,
                username= email,
                telephone = telephone,
                adresse = adresse,
                password = password,
                created_at = created_at,
                updated_at = updated_at,
                roles = roles,
            )
            users.save()
            sweetify.success(request, 'utilisateur ajouté avec succès', button='Fermer', timer=5000)

            personnes_id = Users.objects.filter(email = request.POST['email']).last()
            id= personnes_id.id
            personnes= Personnes.objects.create(
                nom=last_name,
                prenoms=first_name,
                email=email,
                telephone=telephone,
                adresse=adresse,
                users_id=id,
                ddn="1970-01-01"
            )
            personnes.save()

            if request.POST["roles"] == '2':
                medecins_id = Personnes.objects.filter(email = request.POST['email']).last()
                id= medecins_id.id
                medecins= Medecins.objects.create(
                    nom=last_name,
                    prenom=first_name,
                    email=email,
                    telephone=telephone,
                    adresse=adresse,
                    personnes_id=id,
                    specialites_id=""
                )
                medecins.save()
                sweetify.success(request, 'Enregistrement effectué avec succès')

            
           
    else:
            return HttpResponse(form.errors)
   
       
    return HttpResponseRedirect(reverse('users.index'))

def edit(request, id):
        roles = Roles.objects.all()
        users= Users.objects.select_related().get(id=id)
        template = loader.get_template('backend/users/edit.html')
        context = {
            'users': users,
            'roles': roles,
        }
        return HttpResponse(template.render(context, request))
    
        
def update(request, id):
    users = Users.objects.select_related().get(id=id)
    if request.method == "POST":
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        telephone = request.POST['telephone']
        adresse = request.POST['adresse']
        ddn = request.POST['ddn']
        roles = request.POST['roles']
        password = request.POST['password']
        form = EditUsersForm(request.POST, instance=users)
        if form.is_valid():
           
                users.last_name=last_name
                users.first_name=first_name
                users.email=email
                users.telephone = telephone
                users.adresse=adresse
                users.ddn=ddn
                users.roles=Roles.objects.get(id=roles)
                if 'password' in request.POST :
                    users.password = make_password(password)
                users.save()

                personnes_id = Users.objects.filter(email = request.POST['email']).last()
                id= personnes_id.id
                personnes= Personnes.objects.create(
                    nom=last_name,
                    prenoms=first_name,
                    email=email,
                    telephone=telephone,
                    adresse=adresse,
                    ddn="2023-05-20",
                    users_id=id
                )
                personnes.save()

                if request.POST["roles"] == '2':
                    medecins_id = Personnes.objects.filter(email = request.POST['email']).last()
                    id= medecins_id.id
                    medecins= Medecins.objects.create(
                        nom=last_name,
                        prenom=first_name,
                        email=email,
                        telephone=telephone,
                        adresse=adresse,
                        personnes_id=id,
                        specialites_id=""
                    )
                    medecins.save()

        else:
            return HttpResponse(form.errors)
        sweetify.success(request, ' Utilisateur mis à jour avec succès', button='Fermer', timer=5000)
    return HttpResponseRedirect(reverse('users.index'))




def delete(request, id):
   users= Users.objects.get(id=id)
   users.delete()
   sweetify.success(request, 'Utilisateur supprimé avec succès', button='Fermer', timer=5000)
   return HttpResponseRedirect(reverse('users.index'))
