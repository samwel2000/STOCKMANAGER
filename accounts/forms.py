from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(
                attrs = {
                    'required':'true',
                }
            ),
            'last_name':forms.TextInput(
                attrs = {
                    'required':'true',
                }
            ),
        }
