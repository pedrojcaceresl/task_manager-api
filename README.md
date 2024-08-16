# API de Gestión de Tareas

## Descripción

Esta API permite gestionar tareas, categorías, etiquetas y usuarios, proporcionando endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar). Además, implementa autenticación mediante JWT (JSON Web Token).

## Endpoints

### Autenticación

1. **Obtener Token JWT**
   - **Endpoint:** `POST /api/token/`
   - **Descripción:** Obtiene un token JWT para autenticarse.
   - **Ejemplo de Request:**
     ```json
     {
       "username": "usuario",
       "password": "contraseña"
     }
     ```
   - **Ejemplo de Response:**
     ```json
     {
       "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
       "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
     }
     ```

2. **Refrescar Token JWT**
   - **Endpoint:** `POST /api/token/refresh/`
   - **Descripción:** Refresca un token JWT utilizando el token de actualización.
   - **Ejemplo de Request:**
     ```json
     {
       "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
     }
     ```
   - **Ejemplo de Response:**
     ```json
     {
       "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
     }
     ```

### Tareas

1. **Listar todas las tareas**
   - **Endpoint:** `GET /api/tasks/`
   - **Descripción:** Retorna una lista de todas las tareas.
   - **Ejemplo de Response:**
     ```json
     [
       {
         "id": 1,
         "title": "Completar informe de ventas",
         "description": "Informe de ventas mensual para la junta directiva.",
         "status": "pendiente",
         "priority": "alta",
         "due_date": "2024-08-20",
         "category": 1,
         "tags": [1, 2]
       }
     ]
     ```

2. **Crear una nueva tarea**
   - **Endpoint:** `POST /api/tasks/`
   - **Descripción:** Crea una nueva tarea.
   - **Ejemplo de Request:**
     ```json
     {
       "title": "Nueva tarea",
       "description": "Descripción de la nueva tarea",
       "status": "en progreso",
       "priority": "media",
       "due_date": "2024-08-25",
       "category": 2,
       "tags": [3]
     }
     ```
   - **Ejemplo de Response:**
     ```json
     {
       "id": 2,
       "title": "Nueva tarea",
       "description": "Descripción de la nueva tarea",
       "status": "en progreso",
       "priority": "media",
       "due_date": "2024-08-25",
       "category": 2,
       "tags": [3]
     }
     ```

3. **Obtener una tarea específica**
   - **Endpoint:** `GET /api/tasks/{id}/`
   - **Descripción:** Recupera los detalles de una tarea específica.
   - **Ejemplo de Response:**
     ```json
     {
       "id": 1,
       "title": "Completar informe de ventas",
       "description": "Informe de ventas mensual para la junta directiva.",
       "status": "pendiente",
       "priority": "alta",
       "due_date": "2024-08-20",
       "category": 1,
       "tags": [1, 2]
     }
     ```

4. **Actualizar una tarea específica**
   - **Endpoint:** `PUT /api/tasks/{id}/`
   - **Descripción:** Actualiza los detalles de una tarea específica.
   - **Ejemplo de Request:**
     ```json
     {
       "title": "Informe de ventas actualizado",
       "description": "Actualización del informe de ventas",
       "status": "completada",
       "priority": "alta",
       "due_date": "2024-08-20",
       "category": 1,
       "tags": [1, 2]
     }
     ```
   - **Ejemplo de Response:**
     ```json
     {
       "id": 1,
       "title": "Informe de ventas actualizado",
       "description": "Actualización del informe de ventas",
       "status": "completada",
       "priority": "alta",
       "due_date": "2024-08-20",
       "category": 1,
       "tags": [1, 2]
     }
     ```

5. **Eliminar una tarea específica**
   - **Endpoint:** `DELETE /api/tasks/{id}/`
   - **Descripción:** Elimina una tarea específica.
   - **Ejemplo de Response:**
     ```json
     {
       "detail": "Task deleted successfully."
     }
     ```

### Categorías

1. **Listar todas las categorías**
   - **Endpoint:** `GET /api/categories/`
   - **Descripción:** Retorna una lista de todas las categorías.

2. **Crear una nueva categoría**
   - **Endpoint:** `POST /api/categories/`
   - **Descripción:** Crea una nueva categoría.

3. **Obtener una categoría específica**
   - **Endpoint:** `GET /api/categories/{id}/`
   - **Descripción:** Recupera los detalles de una categoría específica.

4. **Actualizar una categoría específica**
   - **Endpoint:** `PUT /api/categories/{id}/`
   - **Descripción:** Actualiza los detalles de una categoría específica.

5. **Eliminar una categoría específica**
   - **Endpoint:** `DELETE /api/categories/{id}/`
   - **Descripción:** Elimina una categoría específica.

### Etiquetas

1. **Listar todas las etiquetas**
   - **Endpoint:** `GET /api/tags/`
   - **Descripción:** Retorna una lista de todas las etiquetas.

2. **Crear una nueva etiqueta**
   - **Endpoint:** `POST /api/tags/`
   - **Descripción:** Crea una nueva etiqueta.

3. **Obtener una etiqueta específica**
   - **Endpoint:** `GET /api/tags/{id}/`
   - **Descripción:** Recupera los detalles de una etiqueta específica.

4. **Actualizar una etiqueta específica**
   - **Endpoint:** `PUT /api/tags/{id}/`
   - **Descripción:** Actualiza los detalles de una etiqueta específica.

5. **Eliminar una etiqueta específica**
   - **Endpoint:** `DELETE /api/tags/{id}/`
   - **Descripción:** Elimina una etiqueta específica.

### Usuarios

1. **Listar todos los usuarios**
   - **Endpoint:** `GET /api/users/`
   - **Descripción:** Retorna una lista de todos los usuarios.

2. **Crear un nuevo usuario**
   - **Endpoint:** `POST /api/users/`
   - **Descripción:** Crea un nuevo usuario.

3. **Obtener un usuario específico**
   - **Endpoint:** `GET /api/users/{id}/`
   - **Descripción:** Recupera los detalles de un usuario específico.

4. **Actualizar un usuario específico**
   - **Endpoint:** `PUT /api/users/{id}/`
   - **Descripción:** Actualiza los detalles de un usuario específico.

5. **Eliminar un usuario específico**
   - **Endpoint:** `DELETE /api/users/{id}/`
   - **Descripción:** Elimina un usuario específico.

## Autenticación

Para acceder a los endpoints que manipulan datos (como crear, actualizar o eliminar), es necesario autenticarse utilizando los endpoints de autenticación. Una vez autenticado, incluye el token JWT en las cabeceras de las solicitudes:

```http
Authorization: Bearer <token>
```

## Ejemplo de uso

### Obtener todas las tareas

```bash
curl -X GET http://localhost:8000/api/tasks/ -H "Authorization: Bearer <token>"
```

### Crear una nueva tarea

```bash
curl -X POST http://localhost:8000/api/tasks/ -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{
  "title": "Nueva tarea",
  "description": "Descripción de la nueva tarea",
  "status": "en progreso",
  "priority": "media",
  "due_date": "2024-08-25",
  "category": 2,
  "tags": [3]
}'
```

## Instalación y configuración

1. **Clonar el repositorio**
   ```bash
   git clone <URL del repositorio>
   cd nombre-del-proyecto
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**
   ```bash
   python manage.py migrate
   ```

4. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

6. **Configuración CORS**
   En el archivo `settings.py`, asegúrate de que CORS está configurado correctamente para permitir el acceso desde todos los orígenes:
   ```python
   CORS_ALLOW_ALL