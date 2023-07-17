from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='agendas.index'),
    path('create/', views.create, name='agendas.create'),
    path('create/store', views.store, name='agendas.store'),
    path('edit/<int:id>/', views.edit, name='agendas.edit'),
    path('edit/update/<int:id>/', views.update, name='agendas.update'),
    path('delete/<int:id>/', views.delete, name='agendas.delete'),
]