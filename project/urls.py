from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcaovoto/", registrar_opcao_voto, name="registrar_opcao_voto"),
]
