from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # VOTAÇÃO
    path("votacao/registrar/<int:id_sala>/", registrar_votacao, name="registrar_votacao"),
    path("votacao/listar/<int:id_sala>/", listar_votacoes, name="listar_votacoes"),
    path("votacao/detalhe/<int:id_votacao>/", detalhe_votacao, name="detalhe_votacao"),

    # OPÇÃO DE VOTO
    path("opcao-voto/registrar/", registrar_opcao, name="registrar_opcao"),
    path("opcao-voto/listar/", listar_opcoes, name="listar_opcoes"),
    
    # sala
    path("sala/registrar/", registrar_sala, name="registrar_sala"),
    path("sala/conectar/", conectar_sala, name="conectar_sala"),

    # APURAÇÃO
    path("votar/<int:id_votacao>/", votar, name="votar"),
    path("apuracao/<int:id_votacao>/", apuracao, name="apuracao"),
    path("apuracao/detalhe/<int:id_votacao>/", detalhe_apuracao, name="detalhe_apuracao"),
]
