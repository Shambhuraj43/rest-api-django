from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),
    path('drinks/<int:id>', views.drink_detail, name='drink_detail')
]
