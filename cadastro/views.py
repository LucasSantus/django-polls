from django.shortcuts import render, redirect
from cadastro.forms import *

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
            pessoa = form.save(commit=False)

            pessoa.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar pessoa",
        "form": form,
    }

    return render(request, "cadastro/registrar_pessoa.html", context)

def registrar_votacao(request):

    form = VotacaoForm()

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
            votacao = form.save(commit=False)

            votacao.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Votação",
        "form": form,
    }

    return render(request, "cadastro/registrar_pessoa.html", context)

def registrar_opcao_voto(request):

    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            opcao_voto = form.save(commit=False)

            opcao_voto.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Opção de Voto",
        "form": form,
    }

    return render(request, "cadastro/registrar_pessoa.html", context)
