from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("votar/<int:id_votacao>", votar, name="votar"),
    path("validacao/<int:id>", validacao, name="validacao"),
]