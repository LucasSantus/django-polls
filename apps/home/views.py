from django.shortcuts import render
from django.utils import timezone
from votacao.models import Votacao
from usuarios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from votacao.models import *

from django.core.paginator import Paginator

def base(request):
    data = timezone.now()
    context = { 
        'data': data.year
    }
    return context

@login_required
def index(request):
    usuario = request.user
    
    list_salas = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').filter(usuarios=usuario).order_by("-data_registrado")
    list_votacoes = Votacao.objects.select_related('sala').filter(sala__in=list_salas)

    list_salas_vinculadas = []

    if not list_salas:
        messages.info(request,"Não existem salas registradas!")

    list_salas_vinculadas = Votacao.get_qtd_votacoes(request, list_salas, list_votacoes)

    context = {
        "salas": list_salas_vinculadas,
    }

    return render(request, "home/index.html", context)

def votacoes(request):
    list_votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    if not votacoes:
        messages.info(request,"No momento não existem votações disponiveis")

    context = {
        "list_votacoes": list_votacoes,
    }
    return render(request, "home/index.html", context)

# Validar se o usuário está cadastrado.
def validate_user(request):
    user = request.GET.get('username', None)
    data = {
        'is_user': Usuario.objects.filter(email__iexact=user).exists(),
    }
    if not data['is_user']:
        data['error_message'] = 'Este e-mail não está cadastrado!'
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_email': Usuario.objects.filter(email__iexact=email).exists(),
    }
    if data['is_email']:
        data['error_message'] = 'Este e-mail já está cadastrado!'
    return JsonResponse(data)

def validate_email_registered(request):
    email = request.GET.get('email', None)
    data = {
        'is_email_registered': Usuario.objects.filter(email__iexact=email).exists(),
    }
    
    if not data['is_email_registered']:
        data['error_message'] = 'Este e-mail não está cadastrado no sistema!'
    return JsonResponse(data)

def validate_group(request):
    group = request.GET.get('sala', None)
    data = {
        'is_group': SalaVotacao.objects.filter(codigo__iexact=group).exists(),
    }
    if not data['is_group']:
        data['error_message'] = 'Este sala não está cadastrado!'
    return JsonResponse(data)