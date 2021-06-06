from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.

class SignUpView(View):
    '''
    View to handle the request for user signup.
    '''

    template_name = 'accounts/signup.html'
    user_form = SignUpForm()

    def get(self, request):
        return render(request, self.template_name, {
            'user_form': self.user_form
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {
            'user_form': form
        })


class ChangePasswordView(View):
    '''
    View to handle request of change password for current user.
    Matches password with old password and changes the password to new password.
    '''

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'accounts/change_password.html', {
            'form': form
        })
