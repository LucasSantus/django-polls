from django.db import models
from django.db.models.fields import BooleanField
from .models import *
from usuarios.models import *

import string
import random

class SalaVotacao(models.Model):
    titulo = models.CharField(
        verbose_name = "Título",
        max_length = 150,
    )

    codigo = models.CharField(
        verbose_name = "Código",
        max_length = 30,
        unique = True,
        null = True,
        blank = True,
    )

    usuarios = models.ManyToManyField(
        Usuario,
        verbose_name = "Usuarios",
        blank = True,
    )

    admin = models.ForeignKey(
        Usuario, 
        on_delete = models.CASCADE,
        verbose_name = "Administrador",
        related_name = "admin",
        null = True,
        blank = True,
    )
    
    is_active = BooleanField(
        default=True
    )

    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação",
        auto_now_add = True,
    )

    class Meta:
        verbose_name = "Sala de Votação"
        verbose_name_plural = "Salas de Votações"

    def __str__(self):
        return self.titulo

class Votacao(models.Model):
    titulo = models.CharField(
        verbose_name = "Título",
        max_length = 150,
    )

    descricao = models.TextField(
        verbose_name = "Descrição",
        max_length = 300,
    )

    anonimo = models.BooleanField(
        verbose_name = "Usuário Anônimo",
        default = False,
    )

    data_inicio = models.DateTimeField(
        verbose_name = "Inicio",
        auto_now = False,
        blank = True,
        null = True,
    )

    data_fim = models.DateTimeField(
        verbose_name = "Término",
        auto_now = False,
        blank = True,
        null = True,
    )
    sala = models.ForeignKey(
        SalaVotacao,
        verbose_name = "Sala de Votação",
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    
    is_active = BooleanField(
        default=True
    )

    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação",
        auto_now_add = True,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"

    def generated_code_random():
        tamanho=16
        valid = True
        while valid == True:
            try:
                codigo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tamanho))
                SalaVotacao.objects.get(codigo=codigo)
            except SalaVotacao.DoesNotExist:
                valid = False
                return codigo

    def get_qtd_votacoes(self, list_salas, list_votacoes):
        vinculo = []
        if list_salas:
            qtd_votacoes = 0
            for sala in list_salas:
                qtd_votacoes = len(list_votacoes.filter(sala=sala))
                obj = {
                    "sala": sala,
                    "qtd_votacoes": qtd_votacoes,
                }
                vinculo.append(obj)
        return vinculo

    def format_date(data):
        date_list = []
        for a in range(16):
            if data[a] != '+' or data[a] != ' ':
                date_list.append(data[a])
            else:
                break
        return "".join(date_list)
    def __str__(self):
        return self.titulo
    
class OpcaoVoto(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 150,
    )

    votacao = models.ForeignKey(
        Votacao,
        verbose_name = "Votação",
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    codigo = models.CharField(
        verbose_name = "Código",
        max_length = 10,
    )

    numero_votos = models.PositiveSmallIntegerField(
        verbose_name = "Número de Voto",
        default = 0,
        null = True,
        blank = True,
    )
    
    is_active = BooleanField(
        default=True
    )

    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação",
        auto_now_add = True,
    )

    class Meta:
        verbose_name = "Opcão de Voto"
        verbose_name_plural = "Opções de Votos"

    def __str__(self):
        return self.nome

class PessoaVoto(models.Model):
    usuario = models.ForeignKey(
        Usuario, 
        on_delete = models.CASCADE
    )

    votacao = models.ForeignKey(
        Votacao, 
        on_delete = models.CASCADE
    )

    opcao_voto = models.ForeignKey(
        OpcaoVoto, 
        on_delete = models.CASCADE
    )

    quantidade_votos = models.IntegerField(
        verbose_name = "Quantidade de Votos",
        null = True,
        default = 0,
    )
    
    is_active = BooleanField(
        default=True
    )

    data_registrado = models.DateTimeField(
        verbose_name = "Data da Criação",
        auto_now_add = True,
    )

    class Meta:
        verbose_name = "Voto da Pessoa"
        verbose_name_plural = "Votos das Pessoas"

    def __str__(self):
        return self.votacao.nome