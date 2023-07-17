from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Users


class LoginForm(AuthenticationForm):
    username = forms.CharField(label= 'Email / Username')
    class Meta(AuthenticationForm):
        fields = ('username', 'password')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'adresse','ddn', 'telephone', 'password1', 'password2')

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ( 'first_name', 'last_name', 'email', 'adresse', 'telephone', 'password','roles')

class EditUsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ( 'first_name', 'last_name', 'email', 'adresse', 'telephone','roles')

    



