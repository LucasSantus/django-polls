from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from usuarios.models import *
from votacao.models import *

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
