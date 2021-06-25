from django.shortcuts import render
from django.utils import timezone
from datetime import date
from django.http import JsonResponse
from votacao.models import Votacao
from usuarios.models import Pessoa
from .colors import Color
from django.contrib import messages

def base(request):
    get_colors = Color.get_colors()
    pessoa = Pessoa.objects.get(id=1)
    if pessoa.mode == "MAIN":
        colors = get_colors["main"]

    elif pessoa.mode == "DARK":
        colors = get_colors["dark"]

    context = { 
        'date': date.today(),
        'colors': colors,
    }
    return context

def index(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    if not votacoes:
        messages.info(request,"No momento não existem votações disponiveis ")

    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)

def mode(request):
    pessoa = Pessoa.objects.get(id=1)
    try:
        mode = request.GET.get('switch-check', False)
    except:
        mode = {}
    
    if mode == "on":
        pessoa.mode = "DARK"
    else: 
        pessoa.mode = "MAIN"
    
    pessoa.save()

    data = {
        'mode': pessoa.mode,
    }

    return JsonResponse(data)