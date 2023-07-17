from django.urls import path
from type_examens import views

urlpatterns = [
    path('', views.index, name='type_examens.index'),
    path('create/', views.create, name='type_examens.create'),
    path('create/store', views.store, name='type_examens.store'),
    path('edit/<int:id>/', views.edit, name='type_examens.edit'),
    path('edit/update/<int:id>/', views.update, name='type_examens.update'),
    path('delete/<int:id>/', views.delete, name='type_examens.delete'),
  
    # Ajoutez ici les autres URLs de votre application 
]