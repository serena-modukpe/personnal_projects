from django.urls import path
from . import views
urlpatterns = [
    path('index/<int:id>/<int:user_id>/<int:dossierpatients_id>/', views.index, name="examenpatients.index"),
    path('create/<int:id>/<int:user_id>', views.create, name="examenpatients.create"),
    path('create/store/<int:id>/<int:user_id>', views.store, name="examenpatients.store"),
    path('edit/<int:id>', views.edit, name="examenpatients.edit"),
    path('edit/update/<int:id>', views.update, name="examenpatients.update"),
    path('delete/<int:id>/', views.delete, name="examenpatients.delete"),
    path('index_patient/<int:dossierpatients_id>/', views.patients, name="examenpatients.index_patient"),
]