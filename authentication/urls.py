from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup', views.signup, name='auth.signup'),
    path('login/', views.customLogin, name='authentication.login'),
    path('logout/', views.userLogout, name='auth.logout'),
    path('login/auth', LoginView.as_view(template_name='frontend/auth/login.html', redirect_authenticated_user=True), name="auth.login"),
    path('activate/<uidb64>', views.activate, name='activate'),
    path('', views.index, name="users.index"),
    path('create/', views.create, name="users.create"),
    path('create/store/', views.store, name="users.store"),
    path('edit/<int:id>', views.edit, name="users.edit"),
    path('edit/update/<int:id>', views.update, name="users.update"),
    path('delete/<int:id>/', views.delete, name="users.delete"),
]