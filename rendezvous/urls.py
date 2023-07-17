from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="rendezvous.index"),
    path('create/', views.create, name="rendezvous.create"),
    path('create/store/', views.store, name="rendezvous.store"),
    path('edit/<int:id>', views.edit, name="rendezvous.edit"),
    path('edit_changer_statut/<int:id>', views.edit_changer_statut, name="rendezvous.edit_changer_statut"),
    #path('edit_changer_statut/update_changer_statut/<int:id>', views.update_changer_statut, name="rendezvous.update_changer_statut"),
    path('edit/update/<int:id>', views.update, name="rendezvous.update"),
    path('delete/<int:id>/', views.delete, name="rendezvous.delete"),
    path('index_patient/', views.patients, name="rendezvous.index_patient"),
    path('index_medecin/', views.mes_patients, name="rendezvous.index_medecin"),
    path('liste_rendezvous/', views.liste_rendezvous, name="rendezvous.liste_rendezvous"),
    path('details/', views.details, name="rendezvous.details"),
    path('details/<int:id>', views.details, name="rendezvous.details"),
    path('ancien_rendez_vous/', views.ancien_rendezvous, name="rendezvous.ancien_rendez_vous"),
    path('changer_statut/<int:id>/<int:user_id>', views.changer_statut, name="rendezvous.changer_statut")
    #path('appointment/', views.appointment, name="rendezvous.appointment"),
    #path('appointment/appointment_store/', views.appointment_store, name="rendezvous.appointment_store"),
]