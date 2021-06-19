from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("votar/<int:id_votacao>/<int:id_pessoa>", votar, name="votar"),
    path("validacao/<int:id_votacao>", validacao, name="validacao"),
    path("apuracao/<int:id_votacao>", apuracao, name="apuracao"),
    path("detalhe-apuracao/<int:id_votacao>", detalhe_apuracao, name="detalhe_apuracao"),
]