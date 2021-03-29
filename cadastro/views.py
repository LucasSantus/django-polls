from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

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

    if request.POST:
        try: 
            cpf = request.POST.get('cpf', None)
            pessoa = Pessoa.objects.get(cpf=cpf)

            if pessoa.cpf == cpf:
                return redirect("votar", id)

        except Pessoa.DoesNotExist: 
            messages.error(request, "hihihi")

    return render(request, "cadastro/validacao.html")