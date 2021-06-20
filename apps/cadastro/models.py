from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = "Nome Completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length=11,
        unique=True,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento",
        auto_now_add=False,
        auto_now=False,
    )

    email = models.EmailField(
        max_length=254,
        verbose_name = "E-mail",
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
        db_table = "pessoa"

    def __str__(self):
        return self.nome

class Votacao(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length=194,
    )

    descricao = models.TextField(
        verbose_name = "Descrição",
        max_length=340,
    )

    anonimo = models.BooleanField(
        verbose_name="Usuário anônimo",
        default=False,
    )

    voto_unico = models.BooleanField(
        default=False,
    )

    data_inicio = models.DateTimeField(
        verbose_name = "Inicio da Votação",
        auto_now=False,
        blank=True,
        null=True,
    )

    data_fim = models.DateTimeField(
        verbose_name = "Término da Votação",
        auto_now=False,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"
        db_table = "votacao"

    def __str__(self):
        return self.nome

class OpcaoVoto(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length=194,
    )

    votacao = models.ForeignKey(Votacao, verbose_name="Votação", on_delete=models.CASCADE)

    codigo = models.CharField(
        verbose_name="Código",
        max_length=194,
    )

    numero_votos = models.PositiveSmallIntegerField(
        verbose_name = "Número de Voto",
        default=0,
    )

    class Meta:
        verbose_name = "Opcão de Voto"
        verbose_name_plural = "Opções de Votos"
        db_table = "opcao"

    def __str__(self):
        return self.nome