# Registro de asistencia

API REST construida con Django y Django REST Framework para registrar la asistencia de estudiantes.

## Instalación

### Crear y activar entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```powershell
pip install -r requirements.txt
```

### Preparar base de datos

```powershell
python manage.py migrate
```

### Ejecutar la aplicación

```powershell
python manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

## Endpoints

### Estado de salud

```text
GET /api/health
```

Respuesta:

```json
{
  "status": "ok"
}
```

### Versión

```text
GET /api/version
```

### Recurso de asistencias

```text
GET    /api/asistencias/
POST   /api/asistencias/
GET    /api/asistencias/{id}/
PUT    /api/asistencias/{id}/
PATCH  /api/asistencias/{id}/
DELETE /api/asistencias/{id}/
```

## Filtro por curso

El listado de asistencias permite filtrar mediante el parámetro `curso`.

Ejemplo:

```text
GET /api/asistencias/?curso=TILE23
```

La búsqueda no distingue entre mayúsculas y minúsculas.

## Pruebas automatizadas

Ejecutar:

```powershell
pytest -v
```

Las pruebas verifican:

- Endpoint de salud.
- Endpoint de versión.
- Listado de asistencias.
- Creación de registros.
- Consulta individual.
- Actualización de registros.
- Eliminación.
- Rechazo de datos incompletos.

## Estructura del proyecto

```text
registro-asistencia/
├── asistencias/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   