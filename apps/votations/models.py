from django.db import models
from .models import *
from autoslug import AutoSlugField
import string, random
from home.models import Base
from django.urls import reverse

class Room(Base):
    title = models.CharField(verbose_name = "Título", max_length = 100, unique = True)
    description = models.TextField(verbose_name = "Descrição", max_length = 2000)
    code = models.CharField(verbose_name = "Código", max_length = 30, unique = True, null = True, blank = True)
    admin = models.ForeignKey("users.User", on_delete = models.CASCADE, verbose_name = "Administrador", related_name = "admin_Rooms_FK", null = True, blank = True,)
    slug = AutoSlugField(populate_from = 'title', unique_with = ['title'], unique = True, editable = True)

    class Meta:
        verbose_name = "Sala de Votação"
        verbose_name_plural = "Salas de Votações"
        db_table = "rooms"
        app_label = "votations"

    def get_desactivate_room(self):
        return reverse('desactivate_room', args = [str(self.id)])

    def get_generated_code():
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        try:
            while Room.objects.get(code = code).exists(): 
                code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        except:
            return code

    def __str__(self):
        return self.title

class Votation(Base):
    titulo = models.CharField(verbose_name = "Título", max_length = 150, unique = True)
    description = models.TextField(verbose_name = "Descrição", max_length = 2000)
    date_starting = models.DateTimeField(verbose_name = "Inicio", auto_now = False, blank = True, null = True)
    date_end = models.DateTimeField(verbose_name = "Término", auto_now = False, blank = True, null = True)
    room = models.ForeignKey("votations.Room", verbose_name = "Sala de Votação", on_delete = models.CASCADE, null = True, blank = True)
    is_user_anonimous = models.BooleanField(verbose_name = "Usuário Anônimo", default = False,)
    slug = AutoSlugField(populate_from = 'title', unique_with = ['title'], unique = True, editable = True)

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"
        db_table = "votations"
        app_label = "votations"

    def __str__(self):
        return self.title

# class OpcaoVoto(models.Model):
#     nome = models.CharField(
#         verbose_name = "Nome",
#         max_length = 150,
#     )

#     votacao = models.ForeignKey(
#         Votacao,
#         verbose_name = "Votação",
#         on_delete = models.CASCADE,
#         null = True,
#         blank = True,
#     )

#     codigo = models.CharField(
#         verbose_name = "Código",
#         max_length = 10,
#     )

#     numero_votos = models.PositiveSmallIntegerField(
#         verbose_name = "Número de Voto",
#         default = 0,
#         null = True,
#         blank = True,
#     )

#     is_active = models.BooleanField(
#         default=True
#     )

#     data_registrado = models.DateTimeField(
#         verbose_name = "Data da Criação",
#         auto_now_add = True,
#     )

#     class Meta:
#         verbose_name = "Opcão de Voto"
#         verbose_name_plural = "Opções de Votos"

#     def __str__(self):
#         return self.nome

# class PessoaVoto(models.Model):
    # usuario = models.ForeignKey(
    #     Usuario, 
    #     on_delete = models.CASCADE
    # )

    # votacao = models.ForeignKey(
    #     Votacao, 
    #     on_delete = models.CASCADE
    # )

    # opcao_voto = models.ForeignKey(
    #     OpcaoVoto, 
    #     on_delete = models.CASCADE
    # )

    # quantidade_votos = models.IntegerField(
    #     verbose_name = "Quantidade de Votos",
    #     null = True,
    #     default = 0,
    # )
    
    # is_active = models.BooleanField(
    #     default=True
    # )

    # data_registrado = models.DateTimeField(
    #     verbose_name = "Data da Criação",
    #     auto_now_add = True,
    # )

    # class Meta:
    #     verbose_name = "Voto da Pessoa"
    #     verbose_name_plural = "Votos das Pessoas"

    # def __str__(self):
    #     return self.votacao.nome
