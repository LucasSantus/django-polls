from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def validacao(request, id):
    if request.POST:
        cpf = request.POST.get('cpf', None)
        try: 
            pessoa = Pessoa.objects.get(cpf=cpf)
            return redirect("votar", id)

        except Pessoa.DoesNotExist: 
            messages.error(request, "CPF não cadastrado!")
    return render(request, "administracao/validacao.html")

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

    return render(request, "administracao/votar.html", context)

