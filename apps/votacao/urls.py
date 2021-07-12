from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Registrar
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcao-voto/", registrar_opcao, name="registrar_opcao"),

    # Listar
    path("listar-votacoes/", listar_votacoes, name="listar_votacoes"),
    path("listar-opcoes/", listar_opcoes, name="listar_opcoes"),
    
    # Detalhes
    path("detalhe-votacao/<int:id_votacao>", detalhe_votacao, name="detalhe_votacao"),
]
