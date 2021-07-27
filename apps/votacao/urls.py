from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # VOTAÇÃO
    path("votacao/registrar/", registrar_votacao, name="registrar_votacao"),
    path("votacao/listar/", listar_votacoes, name="listar_votacoes"),
    path("votacao/detalhe/<int:id_votacao>/", detalhe_votacao, name="detalhe_votacao"),

    # OPÇÃO DE VOTO
    path("opcao-voto/registrar/", registrar_opcao, name="registrar_opcao"),
    path("opcao-voto/listar/", listar_opcoes, name="listar_opcoes"),
    
    # GRUPO
    path("grupo/registrar/", registrar_grupo_votacao, name="registrar_grupo_votacao"),
    path("grupo/conectar/", conectar_grupo, name="conectar_grupo"),

    # APURAÇÃO
    path("votar/<int:id_votacao>/", votar, name="votar"),
    path("apuracao/<int:id_votacao>/", apuracao, name="apuracao"),
    path("apuracao/detalhe/<int:id_votacao>/", detalhe_apuracao, name="detalhe_apuracao"),
]
