from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='consultations.index'),
    path('create/', views.create, name='consultations.create'),
    path('create/store', views.store, name='consultations.store'),
    path('edit/<int:id>/', views.edit, name='consultations.edit'),
    path('edit/update/<int:id>/', views.update, name='consultations.update'),
    path('delete/<int:id>/', views.delete, name='consultations.delete'),
  
    # Ajoutez ici les autres URLs de votre application 
]
