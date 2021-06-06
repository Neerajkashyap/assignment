from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Sign Up Form
class CustomSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    password = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'name',
            'password',
            ]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password > 6 or password < 6:
            raise forms.ValidationError(
                self.error_messages['password Should be 6 digits long'],
                code='password_mismatch',
            )
        if not password.isdigit():
            raise forms.ValidationError(
                "password should be numeric.",
                code='password_mismatch',
            )
        return password