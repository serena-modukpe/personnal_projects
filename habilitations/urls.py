from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='habilitations.index'),
    path('create/', views.create, name='habilitations.create'),
    path('create/store', views.store, name='habilitations.store'),
    path('edit/<int:id>/', views.edit, name='habilitations.edit'),
    path('edit/update/<int:id>/', views.update, name='habilitations.update'),
    path('delete/<int:id>/', views.delete, name='habilitations.delete'),
  
    # Ajoutez ici les autres URLs de votre application 
]