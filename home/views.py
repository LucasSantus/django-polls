from django.shortcuts import render, redirect
from cadastro.models import Votacao

def index(request):

    votacoes = Votacao.objects.all()

    context = {
        "votacoes": votacoes,
    }

    return render(request, "home/index.html", context)