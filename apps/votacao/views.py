from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from usuarios.models import Usuario
from votacao.models import SalaVotacao, Votacao
from django.contrib import messages
from django.utils import timezone

# VOTAÇÃO
# *ORGANIZADO
def registrar_votacao(request, id_sala):
    sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(id = id_sala)

    form = VotacaoForm()
    if request.POST:
        form = VotacaoForm(request.POST)
        if form.is_valid():
            votacao = form.save(commit = False)
            votacao.sala = sala
            votacao.save()
            messages.success(request,"Votação registrada com sucesso!")
            return redirect('listar_votacoes', sala.id)

    context = {
        "form": form,
        "usuario": request.user,
        "sala": sala,
    }

    return render(request, "votacao/votacao/registrar.html", context)

# *ORGANIZADO
def editar_votacao(request, id_votacao):
    votacao = Votacao.objects.select_related('sala').get(id=id_votacao)

    form = VotacaoForm(instance=votacao)
    if request.POST:
        form = VotacaoForm(request.POST, instance=votacao)
        if form.is_valid():
            form.save()
            messages.success(request,"Votação modificada com sucesso!")
            return redirect('listar_votacoes', votacao.sala.id)

    context = {
        "form": form,
    }

    return render(request, 'votacao/votacao/editar.html', context)

# *ORGANIZADO
def listar_votacoes(request, id_sala):
    # list_votacoes = Votacao.objects.filter(sala_id=sala.id, data_inicio__lte=timezone.now(), data_fim__gte=timezone.now()).order_by("-data_registrado")
    
    list_votacoes = Votacao.objects.select_related('sala').filter(sala_id=id_sala, data_inicio__lte=timezone.now(), data_fim__gte=timezone.now()).order_by("-data_registrado")
    votacao = list_votacoes.last()

    context = {
        "list_votacoes": list_votacoes,
        "sala": votacao.sala,
    }

    if not list_votacoes:
        messages.info(request,"Não há votações registradas!")

    return render(request, "votacao/votacao/listar.html", context)

# *ORGANIZADO
def detalhe_votacao(request, id_votacao):
    votacao = Votacao.objects.select_related('sala').get(id=id_votacao)

    context = {
        "votacao": votacao,
    }

    return render(request, "votacao/votacao/detalhe.html", context)

# def desativar_votacao(request, id_votacao):
#     votacao = Votacao.objects.select_related('sala').get(id=id_votacao)

#     form = VotacaoForm(instance=votacao)
#     if request.POST:
#         form = VotacaoForm(request.POST, instance=votacao)
#         if form.is_valid():
#             votacao = form.save(commit=False)
#             votacao.is_active = False
#             votacao.save()
#             messages.success(request,"Votação desativada com sucesso!")
#             return redirect('listar_votacoes', votacao.sala.id)

#     context = {
#         "form": form,
#     }

#     return render(request, 'votacao/votacao/desativar.html', context)

# SALA DE VOTAÇÃO
# *ORGANIZADO
def registrar_sala(request):
    form = SalaVotacaoForm()
    if request.POST:
        form = SalaVotacaoForm(request.POST)
        if form.is_valid():
            sala = form.save(commit = False)
            sala.codigo = Votacao.generated_code_random()
            sala.admin = request.user
            sala.save()
            sala.usuarios.add(request.user)
            messages.success(request,"Sala de Votação registrada com sucesso!")
            return redirect("index")

    context = {
        "form": form,
        "usuario": request.user,
    }

    return render(request, "votacao/sala/registrar.html", context)

# *ORGANIZADO
def editar_sala(request, id_sala):
    sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(id = id_sala)

    form = SalaVotacaoForm(instance=sala)
    if request.POST:
        form = SalaVotacaoForm(request.POST, instance=sala)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.codigo = sala.codigo
            sala.admin = request.user
            sala.save()
            messages.success(request,"Sala modificada com sucesso!")
            return redirect('listar_votacoes', sala.id)

    context = {
        "form": form,
    }

    return render(request, 'votacao/sala/editar.html', context)

# *ORGANIZADO
def conectar_sala(request):

    if request.POST: 
        codigo = request.POST.get("sala", False)
        try:
            sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(codigo__icontains=codigo, usuarios=request.user)
            if sala:
                messages.error(request, f"Você já está conectado(a) a sala: {sala.titulo}!")
        except:
            sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(codigo__icontains=codigo)
            if sala:
                messages.success(request, f"Você conectou a sala: {sala.titulo}!")
                sala.usuarios.add(request.user)
        return redirect("index")

    return render(request, "votacao/sala/conectar.html")

# OPÇÕES DE VOTO
# *ORGANIZADO
def registrar_opcao(request, id_votacao):
    votacao = Votacao.objects.select_related('sala').get(id=id_votacao)

    form = OpcaoVotoForm()
    if request.POST:
        form = OpcaoVotoForm(request.POST)
        if form.is_valid():
            opcao_voto = form.save(commit = False)
            opcao_voto.votacao = votacao
            opcao_voto.save()
            messages.success(request,"Opção de Voto registrada com sucesso!")
            return redirect("votar", votacao.id)

    context = {
        "form": form,
        "votacao": votacao,
    }

    return render(request, "votacao/opcao_voto/registrar.html", context)

# *ORGANIZADO
def editar_opcao(request, id_opcao):
    opcao_voto = OpcaoVoto.objects.select_related('votacao').get(id = id_opcao)

    form = OpcaoVotoForm(instance=opcao_voto)
    if request.POST:
        form = OpcaoVotoForm(request.POST, instance=opcao_voto)
        if form.is_valid():
            form.save()
            messages.success(request,"Opção de Voto modificada com sucesso!")
            return redirect('votar', opcao_voto.votacao.id)

    context = {
        "form": form,
        "votacao": opcao_voto.votacao,
    }

    return render(request, 'votacao/opcao/editar.html', context)

# VOTAR
def votar(request, id_votacao):
    votacao = Votacao.objects.select_related('sala').get(id=id_votacao)
    list_opcoes = OpcaoVoto.objects.select_related('votacao').filter(votacao=votacao)

    if PessoaVoto.objects.select_related('usuario','votacao','opcao_voto').filter(usuario=request.user, votacao=votacao):
        messages.error(request,"Você ja votou!")
        return redirect('listar_votacoes', votacao.sala.id) 

    if request.POST:
        id_opcao_voto = request.POST.get('voto', None)
        opcao_voto = OpcaoVoto.objects.get(pk=id_opcao_voto)
    
        try:
            voto = PessoaVoto.objects.select_related('usuario','votacao','opcao_voto').get(votacao=votacao, usuario=request.user, opcao_voto=opcao_voto)
            opcao_voto.numero_votos += 1
            opcao_voto.save()

        except PessoaVoto.DoesNotExist:
            voto = PessoaVoto()
            voto.usuario = request.user
            voto.opcao_voto = opcao_voto
            voto.votacao = votacao
            voto.quantidade_votos +=1
            voto.save()

        return redirect('listar_votacoes', votacao.sala.id)

    context = {
        "votacao": votacao,
        "list_opcoes": list_opcoes,
    }

    return render(request, "votacao/voto/votar.html", context)

# APURAÇÃO
def apuracao(request, id_votacao):
    votacao = Votacao.objects.get(id = id_votacao)
    
    votos = OpcaoVoto.objects.filter(votacao = votacao)

    context = {
        "votos": votos,
        "votacao": votacao,
    }

    return render(request, "votacao/voto/apuracao.html", context)

def detalhe_apuracao(request, id_votacao):
    
    opcao = OpcaoVoto.objects.get(pk=id_votacao)

    opcoes = PessoaVoto.objects.filter(opcao=opcao)

    context = {
        "opcoes": opcoes,
    }

    return render(request, "administracao/detalhe_apuracao.html", context)
