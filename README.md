************Grupo 2***************************

pasos

- cd microservicio
-python3 -m venv venv
-source venv/bin/activate
-pip install django
-django-admin startproject auth_service
-cd auth_service
-pip install djangorestframework
-python manage.py makemigrations
-python manage.py migrate
-python manage.py runserver
