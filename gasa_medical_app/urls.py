"""
URL configuration for gasa_medical_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roles import views





urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('apropos/', views.about, name='apropos'),
    path('service/', views.service, name='service'),
    path('appointment/', views.rendezvous, name='appointment'),
    path('prix/', views.prix, name='prix'),
    path('team/', views.team, name='team'),
    path('temoignage', views.temoignage, name='temoignage'),
    path('contact/', views.contact, name='contact'),
    #path('signup', views.signup, name='signup'),
    path('connexion/', views.connexion, name='connexion'),
    path('dashbord/', views.dashbord, name='dashbord'),
    path('dashboard_patient/', views.dashbord_patient, name='dashboard_patient'),
    path('dashboard_medecin/', views.dashboard_medecin, name='dashboard_medecin'),
    path('roles/', include('roles.urls')),
    path('habilitations/', include('habilitations.urls')),
    path('consultations/', include('consultations.urls')),
    path('authentication/', include('authentication.urls')),
    path('agendas/', include('agendas.urls')),
    path('specialites/', include('specialites.urls')),
    path('personnes/',include('personnes.urls')),
    path('heures/',include('heures.urls')),
    path('jours/',include('jours.urls')),
    path('medecins/',include('medecins.urls')),
    path('dossierpatients/',include('dossierpatients.urls')),
    path('examenpatients/',include('examenpatients.urls')),
    path('prescriptions/',include('prescriptions.urls')),
    path('habilitations/',include('habilitations.urls')),
    path('consultationpatients/',include('consultationpatients.urls')),
    path('rendezvous/',include('rendezvous.urls')),
    path('type_examens/',include('type_examens.urls')),
    path('conseils_medicaux/',include('conseils_medicaux.urls')),
    path('statut/',include('statut.urls')),
    path('roles_habilitations/',include('roles_habilitations.urls')),
    path('admin/', admin.site.urls),
    
]
