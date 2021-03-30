from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .models import Pessoa_Voto

def validacao(request, id_votacao):
    if request.POST:
        try: 
            cpf = request.POST.get('cpf', None)
            votacao = Votacao.objects.get(pk=id_votacao)
            pessoa = Pessoa.objects.get(cpf=cpf)
            
            if votacao.voto_unico:
                pessoa_voto = Pessoa_Voto.objects.get(votacao=votacao, pessoa=pessoa)

                messages.error(request, "Você ja votou seu safado")
            
        except Pessoa.DoesNotExist: 
            messages.error(request, "CPF não cadastrado!")
        
        except Pessoa_Voto.DoesNotExist: 
           return redirect("votar", id_votacao, pessoa.id)
         
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
            
            objOpcaoVoto.quantidade_votos += 1
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
        
    votacao = Votacao.objects.get(pk=id_votacao)

    votos = OpcaoVoto.objects.filter(votacao=votacao)

    context = {
        "votos": votos,
    }

    return render(request, "administracao/apuracao.html", context)
