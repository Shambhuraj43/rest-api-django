# DJANGO REST API Application

# Dependencies

```
asgiref==3.5.2
certifi==2022.12.7
charset-normalizer==2.1.1
Django==4.1.4
djangorestframework==3.14.0
idna==3.4
python-dotenv==0.21.0
pytz==2022.6
requests==2.28.1
sqlparse==0.4.3
urllib3==1.26.13
```

## Create Django project

## Apply Migrations

`python3 manage.py migrate`

# Create superuser

`python3 manage.py createsuperuser`

# Vault Secrets

1. Install python-dotenv using pip
2. Create .env file with Secrets
3. Fetch Secrets

```python
from os import getenv
from dotenv import load_dotenv
    
    load_dotenv()
    SECRET = getenv('ENV_SECRET_VARIABLE')
```

# Create a separate django app called "api"

1. Register app in [settings.py](http://settings.py/)

# Create models for api app

1. Register new models in [admin.py](http://admin.py/) of the app

```python
from django.contrib import admin
from api.models import Drink
    
    # Register your models here.
    admin.site.register(Drink)
```

1. Apply migrations for the app and the project

 `python3 manage.py migrate` 

`python3 manage.py makemigrations <app_name>`

# Models

- Create a simple model (column)
    
    ```python
    from django.db import models
    
    # Create your models here.
    class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    # # String representation.
    
    def **str**(self):
    return [self.name](http://self.name/) + ' ' + self.description
    
    ```
    

# Django Rest Framework

1. Add  `rest_framework` in installed apps in [settings.py](http://settings.py/)
2. Create `serializers.py` for the application `api`
3. Create a class to serialize the `Drink` model

### RETRIEVE in CRUD

```python

from rest_framework import serializers
from api.models import Drink
    
    class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
    model = Drink
    fields = ['id', 'name', 'description']
```

## Views for Drinks

1. Create a view that will use the serializer `DrinkSerializer`
2. Necessary Imports:

```python
from django.http import JsonResponse
from api.models import Drink
from api.serializers import DrinkSerializer
```

1. Finally, create the view with 3 simple steps:

```python
from django.http import JsonResponse
from api.models import Drink
from api.serializers import DrinkSerializer

# Create your views here.

def drink_list(request):
    # get all the drinks
    # serialize them
    # return JSON

    # Get all the drinks.
    drinks = Drink.objects.all()

    # Serialize them.
    serializer = DrinkSerializer(drinks, many=True)

    # Return JSON.
    return JsonResponse({'drinks': serializer.data})
```

1. Add an endpoint in [urls.py](http://urls.py) for this view

```python
from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('drinks/', views.drink_list, name='drinks'),
]
```

# CRUD

## Get Request == Read / Retrieve Data

- Created a serializer for the Drink model
- Used the serializer to serialize various `drink` objects which existed in the database.
    
    `serializer = DrinkSerializer(drinks, many=True)`
    
- Returned the JsonResponse of the serialized data.

## POST Request == Create Data

## PUT Request == Update Data

## DELETE Request == Delete Data

`views.py`

```
from django.http import JsonResponse
from api.models import Drink
from api.serializers import DrinkSerializer
# Import Decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    # get all the drinks
    # serialize them
    # return JSON

    if request.method == 'GET':
        # Get all the drinks.
        drinks = Drink.objects.all()

        # Serialize them.
        serializer = DrinkSerializer(drinks, many=True)

        # Return JSON.
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    
    try:
        # Get the object with specific id
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        # If object does not exists, throw 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

`urls.py`

```python
from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),
    path('drinks/<int:id>', views.drink_detail, name='drink_detail'),
]
```

## Json Formatting : accessing url [`http://127.0.0.1:8000/drinks.json`](http://127.0.0.1:8000/drinks.json)

- This returns list of drinks in JSON format
- Modify `[urls.py](http://urls.py)` :

```python
from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),
    path('drinks/<int:id>', views.drink_detail, name='drink_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

- In `[views.py](http://views.py)` , in views, add the parameter `format=None` with `request` parameter for each view.

```python
def drink_list(request, format=None):
```

```python
def drink_detail(request, id, format=None):
```