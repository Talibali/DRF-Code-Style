from django.shortcuts import render

# Create your views here.

''' There are 4 ways to create Auth Token
1. From Admin panel ->Need to install (settings.py) package 'rest_framework.authtoken', run migrate command 
2. By command
    python manage.py drf_create_token <username> -> this command will return token
3. By Exposing an API (Custom create API as like in auth.py  and access from url POST http://127.0.0.1:8000/gettoken username:"", Password:"")
4. By signals as like in signals.py when create a user in admin panel
'''