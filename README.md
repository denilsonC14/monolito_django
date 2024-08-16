# Grupo 2 - Monolitica  de Autenticación y tareas
1. Arquitectura Monolítica

El proyecto está estructurado como una única aplicación Django, lo que significa que todo el código, desde las rutas hasta las vistas y los modelos, reside en un solo proyecto. Esta es la definición clásica de una arquitectura monolítica. En lugar de dividirse en múltiples servicios o microservicios, toda la funcionalidad se encuentra en un solo código base, gestionado por un único servidor.

3. CRUD Completo (Crear, Leer, Actualizar, Eliminar)
El proyecto implementa un CRUD completo para la entidad TareaEscolar:

Crear (Create):
La función create en el TareaEscolarViewSet permite a los usuarios crear nuevas tareas escolares. Además, en este proceso se verifica si la fecha de entrega coincide con un día festivo, y si es así, se incluye una advertencia en la descripción.

Leer (Read):
La función get_queryset en el TareaEscolarViewSet se utiliza para leer (obtener) las tareas escolares del usuario autenticado.

Actualizar (Update):
Las tareas pueden ser actualizadas utilizando las vistas basadas en clases (RetrieveUpdateAPIView) o directamente mediante la vista de conjunto (ModelViewSet).

Eliminar (Delete):
Las tareas también pueden ser eliminadas utilizando la vista de conjunto (ModelViewSet), cumpliendo con la funcionalidad de eliminación dentro del CRUD.

3. Sistema de Login
El proyecto tiene implementado un sistema de autenticación y autorización para controlar el acceso a la aplicación:

Registro:
La vista RegisterView permite a los usuarios registrarse en la aplicación.

Login:
La vista LoginView permite a los usuarios autenticarse, devolviendo un token de autenticación. Este token es luego utilizado para acceder a las funcionalidades protegidas de la API.

Autorización:
La autenticación basada en tokens se configura en DEFAULT_AUTHENTICATION_CLASSES, lo que garantiza que solo los usuarios autenticados puedan acceder a los recursos. Las vistas están protegidas por la clase de permisos IsAuthenticated, lo que asegura que solo los usuarios autenticados puedan realizar operaciones CRUD en TareaEscolar.

4. Consumo de una API de terceros
El proyecto hace uso de la función es_dia_festivo para consultar una API de terceros:

API de días festivos:
La función es_dia_festivo utiliza la API de Nager.Date (https://date.nager.at) para obtener los días festivos en un país específico y determinar si una fecha de entrega coincide con un día festivo. Esto se integra en la lógica del negocio al crear una nueva TareaEscolar, añadiendo una advertencia si la fecha de entrega es un día festivo.
Resumen:
Arquitectura Monolítica: El proyecto está organizado como una sola aplicación Django.
CRUD Completo: Implementado para la entidad TareaEscolar.
Sistema de Login: Implementado con autenticación basada en tokens.
Consumo de API de terceros: Implementado mediante la API de días festivos.
Este proyecto cumple con todos los requisitos especificados, integrando correctamente cada componente solicitado.


## Pasos de Configuración


1. Clona este repositorio y navega al directorio del microservicio:
    ```bash
    https://github.com/denilsonC14/monolito_django
    cd auth_service
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

6. Navega al directorio del proyecto y configura el entorno para la creacion de las apis:
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
    - **Contenido tipo :** `application/json`
    - **ejemplo:**  `{
  "username": "usuario123",
  "email": "usuario@example.com",
  "password": "passwordseguro"
}`
  
- **Iniciar sesión:**
    - **Método:** `POST`
    - **URL:** `http://localhost:8000/api/login/`
    -  - **ejemplo:**  `{
  "username": "usuario123",
  "password": "passwordseguro"
}`

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
11. Gestión de Tareas Escolares
    Todas las rutas relacionadas con las tareas están protegidas y requieren un token de autenticación.
    - **Creacion de una tarea :**
    - **Método:** `POST` 
    - **URL:** `http://localhost:8000/api/tareas/` 
    - **Headers:**
        ```plaintext
        Content-Type: application/json
        Authorization: Token <token_obtenido_del_login>
         - **ejemplo:**  `{
  "titulo": "Estudiar para el examen",
  "descripcion": "Matemáticas y Ciencias",
  "fecha_entrega": "2024-08-14",
  "completada": false
}`

-**La API verificará si la fecha_entrega coincide con un día festivo y añadirá una advertencia en la descripción si es así**
## 
12. Listar tareas:
-**GET /api/tareas/**
-**Authorization: Token yourauthtoken**
##
14. Actualizar una tarea:
-**PUT /api/tareas/{id}/**
-**Authorization: Token yourauthtoken**
-**Content-Type: application/json**
##
16. eliminar una tareas
-**DELETE /api/tareas/{id}/**
-**Authorization: Token yourauthtoken**

    

## Estructura del Proyecto

-authentication/: Contiene los modelos, vistas, serializadores y rutas relacionadas con la autenticación y la gestión de usuarios y Implementa el CRUD para la entidad TareaEscolar, que permite a los usuarios gestionar sus tareas.
-urls.py: Define las rutas para los diferentes endpoints de la API.
-Contiene funciones utilitarias como es_dia_festivo, que verifica si una fecha es un día festivo utilizando una API externa.
## API Externa Utilizada
Nager.Date API: Esta API se utiliza para verificar si una fecha específica coincide con un día festivo en un país dado.

Este `README.md` incluye instrucciones para la instalación y uso del proyecto, así como una descripción general de las funcionalidades y cómo contribuyen a los requisitos solicitados.


********

