from django.shortcuts import render
from django.utils import timezone
from datetime import date
from django.http import JsonResponse
from cadastro.models import Votacao
from .colors import Color

def base(request):
    get_colors = Color.get_colors()
    colors = get_colors["main"]
        
    context = { 
        'date': date.today(),
        'colors': colors,
    }
    return context

def index(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)

def mode(request):
    
    try:
        mode = request.GET.get('switch-check', False)
    except:
        mode = {}
        
    if mode == "on":
        print("\n\n\ndark\n\n\n")
    else: 
        print("\n\n\nmain\n\n\n")
        
    data = {
        'mode': mode,
    }

    print("\n\n\n")
    print(mode)
    print("\n\n\n")
    
    return JsonResponse(data)
    
