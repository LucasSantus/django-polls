from django.db import models
from .models import *
from usuarios.models import *

class GrupoVotacao(models.Model):
    titulo = models.CharField(
        verbose_name = "Título:",
        max_length = 194,
    )

    codigo = models.CharField(
        verbose_name = "Código:",
        max_length = 194,
    )
    
    usuario = models.ForeignKey(
        Usuario,
        verbose_name = "Usuario:",
        on_delete = models.CASCADE
    )

    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação:",
        auto_now = True,
    )

    class Meta:
        verbose_name = "Grupo de Votação"
        verbose_name_plural = "Grupos de Votações"

    def __str__(self):
        return self.titulo

class Votacao(models.Model):
    titulo = models.CharField(
        verbose_name = "Título:",
        max_length = 194,
    )

    descricao = models.TextField(
        verbose_name = "Descrição:",
        max_length = 340,
    )

    anonimo = models.BooleanField(
        verbose_name = "Usuário Anônimo:",
        default = False,
    )

    data_inicio = models.DateTimeField(
        verbose_name = "Inicio:",
        auto_now = False,
        blank = True,
        null = True,
    )

    data_fim = models.DateTimeField(
        verbose_name = "Término:",
        auto_now = False,
        blank = True,
        null = True,
    )
    
    grupo = models.ForeignKey(
        GrupoVotacao,
        verbose_name = "Grupo de Votação:",
        on_delete = models.CASCADE
    )
    
    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação:",
        auto_now = True,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"

    def __str__(self):
        return self.titulo

class OpcaoVoto(models.Model):
    nome = models.CharField(
        verbose_name = "Nome:",
        max_length = 194,
    )

    votacao = models.ForeignKey(
        Votacao,
        verbose_name = "Votação:",
        on_delete = models.CASCADE
    )

    codigo = models.CharField(
        verbose_name = "Código:",
        max_length = 194,
    )

    numero_votos = models.PositiveSmallIntegerField(
        verbose_name = "Número de Voto:",
        default = 0,
    )

    class Meta:
        verbose_name = "Opcão de Voto"
        verbose_name_plural = "Opções de Votos"

    def __str__(self):
        return self.nome

class Pessoa_Voto(models.Model):
    pessoa = models.ForeignKey(
        Usuario, 
        on_delete = models.CASCADE
    )

    votacao = models.ForeignKey(
        Votacao, 
        on_delete = models.CASCADE
    )

    opcao = models.ForeignKey(
        OpcaoVoto, 
        on_delete = models.CASCADE
    )

    quantidade_votos = models.IntegerField(
        verbose_name = "Quantidade de Votos",
        null = True,
        default = 0,
    )

    class Meta:
        verbose_name = "Voto da Pessoa"
        verbose_name_plural = "Voto das Pessoas"

    def __str__(self):
        return self.votacao.nome