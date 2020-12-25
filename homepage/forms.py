from django import forms
from homepage.models import member
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class Registrationform(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']