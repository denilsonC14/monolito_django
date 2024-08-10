************Grupo 2***************************

pasos

- cd microservicio
-python3 -m venv venv
-source venv/bin/activate
-pip install django
-django-admin startproject auth_service
python manage.py startapp authentication
-cd auth_service
-pip install djangorestframework
-python manage.py makemigrations
-python manage.py migrate
-python manage.py createsuperuser
accede a http://localhost:8000/admin/ en tu navegador y inicia sesión con las credenciales del superusuario. Deberías poder ver y gestionar los usuarios desde aquí.
-python manage.py runserver

Endpoints
Registrar un nuevo usuario:
Método: POST
URL: http://localhost:8000/api/register/
Iniciar sesión:
Método: POST
URL: http://localhost:8000/api/login/
Obtener información del usuario:

Método: GET
URL: http://localhost:8000/api/user/1/  (reemplaza '1' con el ID real del usuario)
Headers:
Authorization: Token <token_obtenido_del_login>
Actualizar información del usuario:

Método: PUT (o PATCH para una actualización parcial)
URL: http://localhost:8000/api/user/1/  (reemplaza '1' con el ID real del usuario)
Headers:

Content-Type: application/json
Authorization: Token <token_obtenido_del_login>

Dependencias
Django
Django REST framework

para activar el microservicio  en docker
docker-compose up --build
si hay cambios
docker-compose exec web python manage.py migrate
si quiero crear otro superusuario
docker-compose exec web python manage.py createsuperuser
ahora ingresa al http://localhost:8001/admin/
para los endpoint 
Registrar un nuevo usuario:
Método: POST
URL: http://localhost:8001/api/register/
Iniciar sesión:
Método: POST
URL: http://localhost:8001/api/login/
Obtener información del usuario:

Método: GET
URL: http://localhost:8001/api/user/1/  (reemplaza '1' con el ID real del usuario)
Headers:


Método: PUT (o PATCH para una actualización parcial)
URL: http://localhost:8001/api/user/1/  (reemplaza '1' con el ID real del usuario)
Headers:


********

