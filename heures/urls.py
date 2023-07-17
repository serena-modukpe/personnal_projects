from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='heures.index'),
    path('create/', views.create, name='heures.create'),
    path('create/store/', views.store, name='heures.store'),
    path('edit/<int:id>/', views.edit, name='heures.edit'),
    path('edit/update/<int:id>/', views.update, name='heures.update'),
    path('delete/<int:id>/', views.delete, name='heures.delete'),
]