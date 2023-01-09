from django.urls import path
from . import views

urlpatterns = [
    # path('', views.paginaExterna, name='externa'), # home vazia, sendo 127.0.0.1:8000 do "python manage.py runserver"
    path('', views.paginaExterna, name='externa'), #tela inicial.html
]