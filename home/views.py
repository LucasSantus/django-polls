from django.shortcuts import render, redirect
from cadastro.models import Votacao
from django.utils import timezone

def index(request):

    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    context = {
        "votacoes": votacoes,
    }

    return render(request, "home/index.html", context)