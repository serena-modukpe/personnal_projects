from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dossierpatients.index"),
    path('create/', views.create, name="dossierpatients.create"),
    #
    # path('creer_dossier/<int:id>', views.creer_dossier, name="dossierpatients.creer_dossier"),
    path('create/store/', views.store, name="dossierpatients.store"),
    path('edit/<int:id>', views.edit, name="dossierpatients.edit"),
    path('dossierpatient/<int:id>/', views.creer_patient, name="dossierpatients.dossierpatient"),
    path('edit/update/<int:id>', views.update, name="dossierpatients.update"),
    #path('dossier/<int:id>/<int:user_id>', views.creer, name="dossierpatients.dossier"),
    path('dossier/<int:id>/<int:user_id>', views.dossier, name="dossierpatients.dossier"),
    path('liste_dossiers/<int:id>/', views.liste_dossiers, name='dossierpatients.liste_dossiers'),
    path('delete/<int:id>/', views.delete, name="dossierpatients.delete"),
    path('consultations/', views.consultation, name="dossierpatients.consultations"),
    path('index_patient/', views.mes_dossier, name="dossierpatients.index_patient"),
   
]