from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='statut.index'),
    path('create/', views.create, name='statut.create'),
    path('create/store', views.store, name='statut.store'),
    path('edit/<int:id>/', views.edit, name='statut.edit'),
    path('edit/update/<int:id>/', views.update, name='statut.update'),
    path('delete/<int:id>/', views.delete, name='statut.delete'),
  
]