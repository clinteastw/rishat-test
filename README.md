### Rename .env-example to .env and edit
### Uncomment this in project/settings.py
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'PORT': os.environ.get('POSTGRES_PORT'),
#     }
# }
```
- ## Run with Docker

```python
docker-compose up --build -d
```

Go to <http://localhost:8000>


- ## Without docker

Create virtualenv
```python
python -m venv venv
```

Install dependencies
```python
venv/scripts/activate
pip install -r -requirements.txt
```

Run migrations
```python
python manage.py makemigrations app;
python manage.py migrate;
```

Run app
```python
python manage.py runserver 0.0.0.0:8000
```
Create superuser
```python
python manage.py createsuperuser
```
Go to <http://localhost:8000>