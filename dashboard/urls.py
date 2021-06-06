from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import IndexView, SendEmail, AddNewUser

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='dashboard'),
    path('send_email/', SendEmail.as_view(), name='send_email'),
    path('add_user/', AddNewUser.as_view(), name='add_user'),
]