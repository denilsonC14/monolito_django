# Grupo 2 - Microservicio de Autenticación

## Pasos de Configuración

1. Clona este repositorio y navega al directorio del microservicio:
    ```bash
    cd microservicio
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala Django:
    ```bash
    pip install django
    ```

4. Crea un nuevo proyecto Django llamado `auth_service`:
    ```bash
    django-admin startproject auth_service
    ```

5. Crea una nueva aplicación llamada `authentication`:
    ```bash
    python manage.py startapp authentication
    ```

6. Navega al directorio del proyecto y configura el entorno:
    ```bash
    pip install djangorestframework
    ```

7. Realiza las migraciones y crea la base de datos:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

9. Accede al panel de administración:
    - Abre tu navegador y visita: `http://localhost:8000/admin/`.
    - Inicia sesión con las credenciales del superusuario que creaste.

10. Inicia el servidor:
    ```bash
    python manage.py runserver
    ```

## Endpoints

- **Registrar un nuevo usuario:**
    - **Método:** `POST`
    - **URL:** `http://localhost:8000/api/register/`
  
- **Iniciar sesión:**
    - **Método:** `POST`
    - **URL:** `http://localhost:8000/api/login/`

- **Obtener información del usuario:**
    - **Método:** `GET`
    - **URL:** `http://localhost:8000/api/user/1/`  (reemplaza '1' con el ID real del usuario)
    - **Headers:**
        ```plaintext
        Authorization: Token <token_obtenido_del_login>
        ```

- **Actualizar información del usuario:**
    - **Método:** `PUT` (o `PATCH` para una actualización parcial)
    - **URL:** `http://localhost:8000/api/user/1/`  (reemplaza '1' con el ID real del usuario)
    - **Headers:**
        ```plaintext
        Content-Type: application/json
        Authorization: Token <token_obtenido_del_login>
        ```

## Dependencias

- Django
- Django REST framework

## Activar el Microservicio en Docker

Para construir y activar el microservicio utilizando Docker, ejecuta:

```bash
docker-compose up --build

 ## si hay cambios
-docker-compose exec web python manage.py migrate
si quiero crear otro superusuario
-docker-compose exec web python manage.py createsuperuser
-ahora ingresa al http://localhost:8001/admin/
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

docker-compose down 
detener lo eliminar microservicios


********

