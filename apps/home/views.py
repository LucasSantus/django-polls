from django.shortcuts import render
from django.utils import timezone
from votacao.models import Votacao
from usuarios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from votacao.models import *

def base(request):
    data = timezone.now()
    context = { 
        'data': data.year
    }
    return context

@login_required
def index(request):
    user = request.user
    list_grupos = GrupoVotacao.objects.all().order_by('-data_registrado')

    if request.POST:
        pesquisa = request.POST.get("pesquisa", False)
        try:
            list_grupos = GrupoVotacao.objects.filter(titulo__icontains=pesquisa, usuario=user).order_by("-data_registrado")
            if not list_grupos:
                list_grupos = GrupoVotacao.objects.filter(codigo__icontains=pesquisa, usuario=user).order_by("-data_registrado")
                if not list_grupos:
                    messages.error(request, "Grupo não encontrado.")
        except:
            messages.error(request, "Grupo não encontrado.")

    context = {
        "grupos": list_grupos,
    }

    if not list_grupos:
        messages.info(request,"Não existem grupos registrados!")

    return render(request, "votacao/grupo/listar_grupos.html", context)

def votacoes(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    if not votacoes:
        messages.info(request,"No momento não existem votações disponiveis")

    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)