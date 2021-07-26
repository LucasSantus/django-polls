from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Registrar
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcao-voto/", registrar_opcao, name="registrar_opcao"),
    path("registrar-grupos/", registrar_grupo_votacao, name="registrar_grupo_votacao"),

    # Listar
    path("listar-votacoes/", listar_votacoes, name="listar_votacoes"),
    path("listar-opcoes/", listar_opcoes, name="listar_opcoes"),
    path("listar-grupos/", listar_grupos, name="listar_grupos"),
    
    # Detalhes
    path("detalhe-votacao/<int:id_votacao>", detalhe_votacao, name="detalhe_votacao"),

    path("votar/<int:id_votacao>/", votar, name="votar"),
    path("apuracao/<int:id_votacao>", apuracao, name="apuracao"),
    path("detalhe-apuracao/<int:id_votacao>", detalhe_apuracao, name="detalhe_apuracao"),
]
