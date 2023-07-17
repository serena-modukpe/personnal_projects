from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='specialites.index'),
    path('create/', views.create, name='specialites.create'),
    path('create/store', views.store, name='specialites.store'),
    path('edit/<int:id>/', views.edit, name='specialites.edit'),
    path('edit/update/<int:id>/', views.update, name='specialites.update'),
    path('delete/<int:id>/', views.delete, name='specialites.delete'),
  
]