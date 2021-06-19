from django.shortcuts import render
from cadastro.models import Votacao
from django.utils import timezone
from datetime import date

def base(request):
    context = { 
    	'date': date.today()
    }
    return context


def index(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)