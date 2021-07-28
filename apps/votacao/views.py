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
            SalaVotacao.objects.get(codigo=codigo)
        except SalaVotacao.DoesNotExist:
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

# sala
def registrar_sala(request):
    form = SalaVotacaoForm()
    usuario = Usuario.objects.get(id=request.user.id)

    if request.method == "POST":
        form = SalaVotacaoForm(request.POST)
        if form.is_valid():
            sala = form.save(commit = False)
            sala.codigo = code()
            sala.save()
            sala.usuarios.add(usuario)

            messages.success(request,"O novo sala foi inserido com sucesso!")

            return redirect("index")

    context = {
        "form": form,
        "usuario": usuario,
    }

    return render(request, "votacao/sala/registrar_sala.html", context)

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

def conectar_sala(request):
    user = request.user.id

    if request.POST: 
        codigo = request.POST.get("sala", False)

        try:
            sala = SalaVotacao.objects.get(codigo__icontains=codigo, usuarios=user)
            if sala:
                messages.error(request, "Você já está nesse sala.")
        
        except:
            sala = SalaVotacao.objects.get(codigo__icontains=codigo)
            if sala:
                messages.success(request,"Entrou para novo sala.")
                sala.usuarios.add(user)

        return redirect("index")

    return render(request, "votacao/sala/conectar_sala.html")

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
