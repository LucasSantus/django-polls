from django.shortcuts import render


def index(request):

    todos_visitantes = Visitante.objects.order_by("-horario_chegada")

    visitantes_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitantes_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )

    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month=mes_atual
    )

    context = {
        "nome_pagina": "Inicio do dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count,
        "visitantes_em_visita": visitantes_em_visita.count,
        "visitantes_finalizado": visitantes_finalizado.count,
        "visitantes_mes": visitantes_mes.count,
    }

    return render(request, "index.html", context)

    

def registrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.save()

            messages.success(
                request, "Visitante registrado com sucesso!"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar pessoa",
        "form": form,
    }

    return render(request, "registrar_pessoa.html", context)

