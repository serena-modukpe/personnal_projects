from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:id>/<int:user_id>/<int:dossierpatients_id>/', views.index, name="consultationpatients.index"),
    path('create/<int:id>/<int:user_id>/', views.create, name="consultationpatients.create"),
    path('create/store/<int:id>/<int:user_id>/', views.store, name="consultationpatients.store"),
    path('create/store/<int:id>/<int:user_id>/', views.store, name="consultationpatients.index"),
    path('details/<int:id>/', views.details, name="consultationpatients.details"),
    path('edit/<int:id>', views.edit, name="consultationpatients.edit"),
    path('edit/update/<int:id>', views.update, name="consultationpatients.update"),
    path('delete/<int:id>/', views.delete, name="consultationpatients.delete"),
    path('index_patient/<int:dossierpatients_id>/', views.patients, name="consultationpatients.index_patient"),
]