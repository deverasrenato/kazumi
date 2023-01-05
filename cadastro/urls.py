from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # home vazia, sendo 127.0.0.1:8000 do "python manage.py runserver"
]