from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dossierpatients.index"),
    path('create/', views.create, name="dossierpatients.create"),
    path('create/store/', views.store, name="dossierpatients.store"),
    path('edit/<int:id>', views.edit, name="dossierpatients.edit"),
    path('edit/update/<int:id>', views.update, name="dossierpatients.update"),
    path('delete/<int:id>/', views.delete, name="dossierpatients.delete"),
]