import re

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from .forms import CustomSignUpForm

User = get_user_model()


# Create your views here.

def check_numeric_password(password):
    '''
	This will check password for numeric and 6 digit long.
	'''

    if re.match("^[0-9]{6,6}$", password):
        return True
    else:
        return False

class IndexView(View):

    template_name = 'dashboard/index.html'
    context = dict()

    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.all()
            count = User.objects.aggregate(
                address_count=Count('address'),
                mobile_count=Count('phone_number')
            )
            email_list = list()
            for data in user:
                if not data.email in email_list:
                    email_list.append(data.email)
            self.context['user_count'] = user.count()
            self.context['address_count'] = count['address_count']
            self.context['mobile_count'] = count['mobile_count']
            self.context['email_list'] = email_list
            return render(request, self.template_name, self.context)
        else:
            redirect('login')


class SendEmail(View):
    '''
    View to send email to the user.
    '''

    def post(self, request):
        email = request.POST.get('email', None)
        message = request.POST.get('description', None)
        if email and message:
            subject = 'Assignment test email'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return JsonResponse({"message": "Email sent successfully"}, status=200)
        else:
            return JsonResponse({"error": "Both fields are required"}, status=400)


class AddNewUser(View):
    '''
    View to add new user with fields username, name, email, password.
    '''

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        # to check for empty fields
        if not all ((username, password, name, email)):
            return JsonResponse({"error": "All fields are required"}, status=400)
        # to check if username is already taken

        elif User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User with this username already exists"}, status=400)
        
        # to check if password is numeric and six digit long
        elif not check_numeric_password(password):
            return JsonResponse({"error": "Password should be 6 digits"}, status=400)
        else:
            User.objects.create_user(
                username=username,
                email=email,
                first_name =name,
                password = password
            )
            return JsonResponse({"message": "User created successfully"}, status=200)
