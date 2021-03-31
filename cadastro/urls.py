from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcao-voto/", registrar_opcao, name="registrar_opcao"),
    
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),
    path("listar-votacos/", listar_votacoes, name="listar_votacoes"),
    path("listar-opcoes/", listar_opcoes, name="listar_opcoes"),
    
    path("detalhe-votacao/<int:id_votacao>", detalhe_votacao, name="detalhe_votacao"),
]
