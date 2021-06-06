# Assignment Project

## Installation

> $ pip install -r requirements.txt

## Running Project

First run the migrations using following command

> python manage.py migrate

Create superuser using following command

> python manage.py createsuperuser

This user will be your admin user who will have acess to the dashboard

## Email Settings

Change the email settings accordingly in settings.py file

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email address'
EMAIL_HOST_PASSWORD = 'your email password'
```

Make sure to allow access of less secure app in your gmail settings

Then run project using command :

> python manage.py runserver

Now project will be running at localhost. You can access the home page at http://127.0.0.1:8000

## Api Endpoints

The api endpoints for user authentication are as follows :

> For registration : http://127.0.0.1:8000/api/signup/

Method : POST

> For login : http://127.0.0.1:8000/api/rest-auth/login/

Method : POST

> For logout : http://127.0.0.1:8000/api/rest-auth/logout/

Method : POST


