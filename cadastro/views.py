from django.shortcuts import render, redirect
from .forms import *
from .models import *

def registrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
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
            votacao = form.save()
            votacao.save()
            return redirect("index")

    context = {
        "nome_pagina": "Registrar Votação",
        "form": form,
    }

    return render(request, "cadastro/registrar_votacao.html", context)

def registrar_opcao(request):

    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            opcao_voto = form.save()

            opcao_voto.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Opção de Voto",
        "form": form,
    }

    return render(request, "cadastro/registrar_opcao.html", context)

def listar_pessoas(request):

    pessoas = Pessoa.objects.all()

    context = {
        "pessoas": pessoas,
    }

    return render(request, "cadastro/listar_pessoa.html", context)

def votar(request, id_votacao):

    objVotacao = Votacao.objects.get(pk=id_votacao)

    listOpcaoVoto = OpcaoVoto.objects.filter(votacao=objVotacao)
    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)

        objOpcaoVoto.numero_votos += 1
        objOpcaoVoto.save()
        return redirect('index')

    context = {
        "objVotacao": objVotacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "cadastro/votar.html", context)

def validacao(request, id):
    pessoas = Pessoa.objects.all()

    if request.POST:
        for validar in pessoas:
            if validar.cpf == request.POST.get('cpf', None):
                return redirect("votar", id)

    return render(request, "cadastro/validacao.html")