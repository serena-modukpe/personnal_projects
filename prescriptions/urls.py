from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:id>/<int:user_id>/<int:dossierpatients_id>/', views.index, name="prescriptions.index"),
    path('prescriptions/create/<int:id>/<int:user_id>', views.create, name="prescriptions.create"),
    path('create/store/<int:id>/<int:user_id>', views.store, name="prescriptions.store"),
    path('edit/<int:id>', views.edit, name="prescriptions.edit"),
    path('edit/update/<int:id>', views.update, name="prescriptions.update"),
    path('delete/<int:id>/', views.delete, name="prescriptions.delete"),
    path('index_patient/<int:dossierpatients_id>', views.patients, name="prescriptions.index_patient"),
]