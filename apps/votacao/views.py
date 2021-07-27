from django.shortcuts import render, redirect
from .forms import *
from .models import *
from usuarios.models import Usuario
from django.contrib import messages

import string
import random

def code_generated(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def code():
    valid = True
    while valid == True:
        try:
            codigo = code_generated()
            GrupoVotacao.objects.get(codigo=codigo)
        except GrupoVotacao.DoesNotExist:
            valid = False
            return codigo

# VOTAÇÃO
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

def listar_votacoes(request):
    votacoes = Votacao.objects.all()
    context = {
        "votacoes": votacoes,
    }

    if not votacoes:
        messages.info(request,"Não existem votações registradas!")

    return render(request, "votacao/votacao/listar_votacao.html", context)

def detalhe_votacao(request, id_votacao):

    votacao = Votacao.objects.get(pk=id_votacao)

    context = {
        "votacao": votacao,
    }

    return render(request, "votacao/votacao/detalhe_votacao.html", context)

# GRUPO
def registrar_grupo(request):
    form = GrupoVotacaoForm()
    usuario = Usuario.objects.get(id=request.user.id)

    if request.method == "POST":
        form = GrupoVotacaoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit = False)
            grupo.usuario = usuario
            grupo.codigo = code()
            grupo.save()

            messages.success(request,"O novo grupo foi inserido com sucesso!")

            return redirect("listar_grupos")

    context = {
        "form": form,
        "usuario": usuario,
    }

    return render(request, "votacao/grupo/registrar_grupo.html", context)

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

def conectar_grupo(request):
    form = OpcaoVotoForm()
    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form,
    }

    return render(request, "votacao/grupo/conectar_grupo.html", context)

# OPÇÕES DE VOTO
def listar_opcoes(request):
    
    opcoes = OpcaoVoto.objects.all()

    context = {
        "opcoes": opcoes,
    }

    return render(request, "votacao/opcao_voto/listar_opcoes.html", context)

def votar(request, id_votacao):
    pessoa = Usuario.objects.get(pk=request.user.id)
    votacao = Votacao.objects.get(pk=id_votacao)
    listOpcaoVoto = OpcaoVoto.objects.filter(votacao=votacao)

    if Pessoa_Voto.objects.filter(pessoa=pessoa,votacao=votacao) and votacao.voto_unico == True:
        messages.error(request,"O voto é unico!")
        return redirect("index") 

    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)
    
        try:
            voto = Pessoa_Voto.objects.get(votacao=votacao, pessoa=pessoa, opcao=objOpcaoVoto)
            
            objOpcaoVoto.numero_votos += 1
            objOpcaoVoto.save()
            
        except Pessoa_Voto.DoesNotExist:
            voto = Pessoa_Voto()
            
        voto.pessoa = pessoa
        voto.opcao = objOpcaoVoto
        voto.votacao = votacao
        voto.quantidade_votos +=1
            

        voto.save()
        
        return redirect('index')

    context = {
        "objVotacao": votacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "administracao/votar.html", context)

# APURAÇÃO
def apuracao(request, id_votacao):
    
    votacao = Votacao.objects.get(pk=id_votacao)
    
    votos = OpcaoVoto.objects.filter(votacao=votacao)

    context = {
        "votos": votos,
    }

    return render(request, "administracao/apuracao.html", context)

def detalhe_apuracao(request, id_votacao):
        
    opcao = OpcaoVoto.objects.get(pk=id_votacao)

    opcoes = Pessoa_Voto.objects.filter(opcao=opcao)

    context = {
        "opcoes": opcoes,
    }

    return render(request, "administracao/detalhe_apuracao.html", context)
