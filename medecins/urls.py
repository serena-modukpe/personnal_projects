from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="medecins.index"),
    path('create/', views.create, name="medecins.create"),
    path('create/store/', views.store, name="medecins.store"),
    path('edit/<int:id>', views.edit, name="medecins.edit"),
    path('edit/update/<int:id>', views.update, name="medecins.update"),
    path('delete/<int:id>/', views.delete, name="medecins.delete"),
   
]