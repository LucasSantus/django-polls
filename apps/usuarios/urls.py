from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Registrar
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    
    # Listar
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),
]
