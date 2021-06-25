from django.db import models
from votacao.models import *
from usuarios.models import *

class Pessoa_Voto(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, 
        on_delete=models.CASCADE
    )
    votacao = models.ForeignKey(
        Votacao, 
        on_delete=models.CASCADE
    )
    opcao = models.ForeignKey(
        OpcaoVoto, 
        on_delete=models.CASCADE
    )
    quantidade_votos = models.IntegerField(
        verbose_name = "Quantidade de Votos",
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = "Voto Pessoa"
        verbose_name_plural = "Voto das Pessoas"
        db_table = "pessoa_voto"

    def __str__(self):
        return self.votacao.nome