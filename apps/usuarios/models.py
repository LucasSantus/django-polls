from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = "Nome Completo:",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name = "CPF:",
        max_length=11,
        unique=True,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento:",
        auto_now_add=False,
        auto_now=False,
    )

    email = models.EmailField(
        max_length=254,
        verbose_name = "E-mail:",
        unique=True,
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome