# Grupo 2 - Microservicio de Autenticación

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
-La API verificará si la fecha_entrega coincide con un día festivo y añadirá una advertencia en la descripción si es así
12. Listar tareas:
-GET /api/tareas/
-Authorization: Token yourauthtoken
13. Actualizar una tarea:
-PUT /api/tareas/{id}/
-Authorization: Token yourauthtoken
-Content-Type: application/json
14. eliminar una tareas
-DELETE /api/tareas/{id}/
-Authorization: Token yourauthtoken

    

## Estructura del Proyecto

-authentication/: Contiene los modelos, vistas, serializadores y rutas relacionadas con la autenticación y la gestión de usuarios y Implementa el CRUD para la entidad TareaEscolar, que permite a los usuarios gestionar sus tareas.
-urls.py: Define las rutas para los diferentes endpoints de la API.
-Contiene funciones utilitarias como es_dia_festivo, que verifica si una fecha es un día festivo utilizando una API externa.
## API Externa Utilizada
Nager.Date API: Esta API se utiliza para verificar si una fecha específica coincide con un día festivo en un país dado.

Este `README.md` incluye instrucciones para la instalación y uso del proyecto, así como una descripción general de las funcionalidades y cómo contribuyen a los requisitos solicitados.


********

