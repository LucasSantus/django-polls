from django.shortcuts import render, redirect
from cadastro.models import Votacao
from django.utils import timezone

def index(request):

    votacoes = Votacao.objects.filter(data_inicio__lt=timezone.now(), data_fim__gt=timezone.now())
    
    context = {
        "votacoes": votacoes,
    }

    return render(request, "home/index.html", context)