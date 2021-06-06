from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    '''
    Custom user model to add new fields to django user model.
    '''
    address = models.TextField(max_length=500, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
