from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'address',
            'phone_number',
            'password1', 
            'password2', 
            ]