from apps.home.forms import ContatoForm
from django.shortcuts import render, redirect
from django.utils import timezone
from votacao.models import Votacao
from usuarios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from votacao.models import *
from project.settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail

def base(request):
    data = timezone.now()
    context = { 
        'data': data.year
    }
    return context

@login_required
def index(request):
    list_salas = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').filter(usuarios=request.user).order_by("-data_registrado")
    list_votacoes = Votacao.objects.select_related('sala').filter(sala__in=list_salas)

    list_salas_vinculadas = []

    if not list_salas:
        messages.info(request,"Não existem salas registradas!")

    list_salas_vinculadas = Votacao.get_qtd_votacoes(request, list_salas, list_votacoes)

    context = {
        "salas": list_salas_vinculadas,
    }

    return render(request, "home/index.html", context)

@login_required
def contato(request):
    form = ContatoForm()
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            email = form.cleaned_data['email']
            titulo = form.cleaned_data['titulo']
            messagem = form.cleaned_data['messagem']

            text = ("{nome} {sobrenome} deixou uma mensagem," +
                "para entrar em contato," +
                "E-mail: {email}," +
                "A messagem deixada por {nome} é:" +
                "{messagem}")

            try:
                DEFAULT_FROM_EMAIL = 'Votation <lucayasiltos@gmail.com>'
                send_mail(
                    titulo, 
                    text, 
                    DEFAULT_FROM_EMAIL, 
                    ['leos9877@gmail.com']
                )
            except:
                messages.error(request,"Falha ao enviar contato!")

            print(form.errors)

            messages.success(request,"Contato enviado com sucesso!\nEntraremos em contato!")
            return redirect("index")

    context = {
        "form": form,
    }

    return render(request, "contato/contato.html", context)
