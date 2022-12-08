DJANGO REST API Application

# Create a virtual environment


# Dependencies
Django==4.1.4
djangorestframework==3.14.0

# Create Django project

# Apply Migrations
`python3 manage.py migrate`

# Create superuser
`python3 manage.py createsuperuser`

# Vault Secrets
1. Install python-dotenv using pip
2. Create .env file with Secrets
3. Fetch Secrets
    `
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()
    SECRET = getenv('ENV_SECRET_VARIABLE')
    `
# Create a saparate django app called "api"
1. Register app in settings.py

# Create models for api app
0. Register new models in admin.py of the app 
    `
    from django.contrib import admin
    from api.models import Drink

    # Register your models here.
    admin.site.register(Drink)
    `
1. Apply migrations for the app and the project
    `
    python3 manage.py migrate
    python3 manage.py makemigrations <app_name>
    `