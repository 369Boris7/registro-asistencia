# Registro de asistencia

API REST construida con Django REST Framework.

## Instalación

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints

- GET/POST `/api/asistencias/`
- GET/PATCH/PUT/DELETE `/api/asistencias/<id>/`
- GET `/api/health`
- GET `/api/version`
