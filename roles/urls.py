from django.urls import path
from roles import views

urlpatterns = [
    path('', views.index, name='roles.index'),
    path('', views.index, name='roles.index'),
    path('create/', views.create, name='roles.create'),
    path('create/store', views.store, name='roles.store'),
    path('edit/<int:id>/', views.edit, name='roles.edit'),
    path('edit/update/<int:id>/', views.update, name='roles.update'),
    path('dashbordpatient/', views.dashbord_patient, name='dashbordpatient'),
    path('dashboard_medecin/', views.dashboard_medecin, name='dashboard_medecin'),
    path('delete/<int:id>/', views.delete, name='roles.delete'),
    #path('get_agendas/', views.get_agendas, name='get_agendas'),
    path('rendezvous/rendezvous_store/', views.rendezvous_store, name="rendezvous.rendezvous_store"),

  
    # Ajoutez ici les autres URLs de votre application 
]