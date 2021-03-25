from django.shortcuts import render
from cadastro.forms import PessoaForm

def index(request):

    context = {
        "nome_pagina": "Inicio do dashboard",

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

    return render(request, "cadastro/registrar_pessoa.html", context)

