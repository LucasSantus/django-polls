from django.shortcuts import render, redirect
from .forms import *
from .models import *
from usuarios.models import Usuario
from django.contrib import messages

def registrar_votacao(request):
    form = VotacaoForm()
    usuario = Usuario.objects.get(id=request.user.id)

    if request.method == "POST":
        form = VotacaoForm(request.POST)
        if form.is_valid():
            votacao = form.save()
            votacao.save()
            messages.success(request,"A nova votação foi inserida com sucesso!")
            return redirect("index")

    context = {
        "form": form,
        "usuario": usuario,
    }

    return render(request, "votacao/votacao/registrar_votacao.html", context)

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

    return render(request, "votacao/opcao/registrar_opcao.html", context)

def listar_votacoes(request):
    votacoes = Votacao.objects.all()
    context = {
        "votacoes": votacoes,
    }

    if not votacoes:
        messages.info(request,"Não existem votações registradas!")

    return render(request, "votacao/votacao/listar_votacao.html", context)

def listar_opcoes(request):
    
    opcoes = OpcaoVoto.objects.all()

    context = {
        "opcoes": opcoes,
    }

    return render(request, "votacao/opcao_voto/listar_opcoes.html", context)

def detalhe_votacao(request, id_votacao):

    votacao = Votacao.objects.get(pk=id_votacao)

    context = {
        "votacao": votacao,
    }

    return render(request, "votacao/votacao/detalhe_votacao.html", context)