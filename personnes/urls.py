from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="personnes.index"),
    path('create/', views.create, name="personnes.create"),
    path('create/store/', views.store, name="personnes.store"),
    path('edit/<int:id>', views.edit, name="personnes.edit"),
    path('edit/update/<int:id>', views.update, name="personnes.update"),
    path('delete/<int:id>/', views.delete, name="personnes.delete"),
    
]