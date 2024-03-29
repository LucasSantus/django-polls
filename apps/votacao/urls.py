from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [


    # VOTAÇÃO
    path("votacao/registrar/<int:id_sala>/", registrar_votacao, name="registrar_votacao"),
    path("votacao/editar/<int:id_votacao>/", editar_votacao, name="editar_votacao"),
    path("votacao/listar/<int:id_sala>/", listar_votacoes, name="listar_votacoes"),
    path("votacao/detalhe/<int:id_votacao>/", detalhe_votacao, name="detalhe_votacao"),

    # OPÇÃO DE VOTO
    path("opcao/registrar/<int:id_votacao>/", registrar_opcao, name="registrar_opcao"),
    path("opcao/editar/<int:id_votacao>/", editar_opcao, name="editar_opcao"),

    # APURAÇÃO
    path("apuracao/<int:id_votacao>/", apuracao, name="apuracao"),
    path("apuracao/detalhe/<int:id_votacao>/", detalhe_apuracao, name="detalhe_apuracao"),
    
    # VOTAR
    path("votar/<int:id_votacao>/", votar, name="votar"),
]
