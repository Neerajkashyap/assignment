from django.urls import path, include

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='api_signup'),
    path('rest-auth/', include('rest_auth.urls')),
]