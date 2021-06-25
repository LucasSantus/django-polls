

class Votacao(models.Model):
    titulo = models.CharField(
        verbose_name = "Título:",
        max_length=194,
    )

    descricao = models.TextField(
        verbose_name = "Descrição:",
        max_length=340,
    )

    anonimo = models.BooleanField(
        verbose_name="Usuário Anônimo:",
        default=False,
    )

    data_inicio = models.DateTimeField(
        verbose_name = "Inicio:",
        auto_now=False,
        blank=True,
        null=True,
    )

    data_fim = models.DateTimeField(
        verbose_name = "Término:",
        auto_now=False,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"

    def __str__(self):
        return self.titulo

class OpcaoVoto(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length=194,
    )

    votacao = models.ForeignKey(Votacao, verbose_name="Votação:", on_delete=models.CASCADE)

    codigo = models.CharField(
        verbose_name="Código:",
        max_length=194,
    )

    numero_votos = models.PositiveSmallIntegerField(
        verbose_name = "Número de Voto:",
        default=0,
    )

    class Meta:
        verbose_name = "Opcão de Voto"
        verbose_name_plural = "Opções de Votos"

    def __str__(self):
        return self.nome

    
    votacao = Votacao.objects.get(pk=id_votacao)

    context = {
        "votacao": votacao,
    }

    return render(request, "cadastro/detalhe_votacao.html", context)