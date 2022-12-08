from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('drinks/', views.drink_list, name='drinks'),
]
