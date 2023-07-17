from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='jours.index'),
    path('create/', views.create, name='jours.create'),
    path('create/store', views.store, name='jours.store'),
    path('edit/<int:id>/', views.edit, name='jours.edit'),
    path('edit/update/<int:id>/', views.update, name='jours.update'),
    path('delete/<int:id>/', views.delete, name='jours.delete'),
]