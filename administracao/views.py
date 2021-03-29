from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .models import Pessoa_Voto

def validacao(request, id_votacao):
    if request.POST:
        cpf = request.POST.get('cpf', None)
        try: 
            pessoa = Pessoa.objects.get(cpf=cpf)
            return redirect("votar", id_votacao, pessoa.id)

        except Pessoa.DoesNotExist: 
            messages.error(request, "CPF não cadastrado!")
    return render(request, "administracao/validacao.html")

def votar(request, id_votacao, id_pessoa):

    pessoa = Pessoa.objects.get(pk=id_pessoa)
    votacao = Votacao.objects.get(pk=id_votacao)
    listOpcaoVoto = OpcaoVoto.objects.filter(votacao=votacao)

    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)

        try:
            voto = Pessoa_Voto.objects.get(votacao=votacao, pessoa=pessoa, opcao=objOpcaoVoto)

        except Pessoa_Voto.DoesNotExist:
            voto = Pessoa_Voto()

        voto.pessoa = pessoa
        voto.opcao = objOpcaoVoto
        voto.votacao = votacao
        voto.quantidade_votos +=1
        voto.save()

        objOpcaoVoto.numero_votos += 1
        objOpcaoVoto.save()
        return redirect('index')

    context = {
        "objVotacao": votacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "administracao/votar.html", context)