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

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]

            cpf_formatado = f"{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}"

            return cpf_formatado
            
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome