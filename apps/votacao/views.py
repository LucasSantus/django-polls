from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from usuarios.models import Usuario
from votacao.models import SalaVotacao, Votacao
from django.contrib import messages

# VOTAÇÃO
def registrar_votacao(request, id_sala):
    sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(id = id_sala)

    form = VotacaoForm()
    if request.method == "POST":
        form = VotacaoForm(request.POST)
        if form.is_valid():
            votacao = form.save(commit = False)
            votacao.sala = sala
            votacao.save()
            messages.success(request,"A nova votação foi inserida com sucesso!")
            return redirect('listar_votacoes', sala.id)

    context = {
        "form": form,
        "usuario": request.user,
        "sala": sala,
    }

    return render(request, "votacao/votacao/registrar_votacao.html", context)

def editar_votacao(request, id_votacao):
    votacao = Votacao.objects.select_related('sala').get(id=id_votacao)

    form = VotacaoForm(instance=votacao)
    if request.POST:
        form = VotacaoForm(request.POST, instance=votacao)
        if form.is_valid():
            form.save(commit=False)
            return redirect('listar_votacoes', votacao.id)

    context = {
        "form": form,
    }

    return render(request, 'votacao/votacao/editar.html', context)

def listar_votacoes(request, id_sala):
    # sala = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').get(id = id_sala)
    
    # list_votacoes = Votacao.objects.filter(sala_id=sala.id).order_by("-data_registrado")
    # list_votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    list_votacoes = Votacao.objects.select_related('sala').filter(sala_id=id_sala)
    votacao = list_votacoes.last() 

    context = {
        "list_votacoes": list_votacoes,
        "sala": votacao.sala,
    }

    if not list_votacoes:
        messages.info(request,"Não existem votações registradas!")

    return render(request, "votacao/votacao/listar_votacoes.html", context)

def detalhe_votacao(request, id_votacao):
    votacao = Votacao.objects.get(id=id_votacao)

    context = {
        "votacao": votacao,
    }

    return render(request, "votacao/votacao/detalhe_votacao.html", context)

# def desativar_votacao(request, id_votacao):

# SALA DE VOTAÇÃO
def registrar_sala(request):
    form = SalaVotacaoForm()
    usuario = Usuario.objects.get(id=request.user.id)

    if request.POST:
        form = SalaVotacaoForm(request.POST)
        if form.is_valid():
            sala = form.save(commit = False)
            sala.codigo = Votacao.generated_code_random()
            sala.admin = usuario
            sala.save()
            sala.usuarios.add(usuario)

            messages.success(request,"A nova sala de votação foi inserida com sucesso!")

            return redirect("index")

    context = {
        "form": form,
        "usuario": usuario,
    }

    return render(request, "votacao/sala/registrar_sala.html", context)

def editar_sala(request, id_sala):
    obj_sala = get_object_or_404(SalaVotacao, id=id_sala)
    codigo = obj_sala.codigo
    usuario = request.user
    
    if request.POST:
        form = SalaVotacaoForm(request.POST, instance=obj_sala)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.codigo = codigo
            sala.admin = usuario
            sala.save()
            return redirect('listar_votacoes', obj_sala.id)
    else:
        form = SalaVotacaoForm(instance=obj_sala)
        
    context = {
        "form": form,
    }
    return render(request, 'votacao/sala/editar.html', context)

def conectar_sala(request):
    user = request.user.id

    if request.POST: 
        codigo = request.POST.get("sala", False)

        try:
            sala = SalaVotacao.objects.get(codigo__icontains=codigo, usuarios=user)
            if sala:
                messages.error(request, "Você já está nesse sala.")
        
        except:
            sala = SalaVotacao.objects.get(codigo__icontains=codigo)
            if sala:
                messages.success(request,"Entrou para novo sala.")
                sala.usuarios.add(user)

        return redirect("index")

    return render(request, "votacao/sala/conectar_sala.html")

# OPÇÕES DE VOTO
def registrar_opcao(request, id_votacao):
    form = OpcaoVotoForm()
    votacao = Votacao.objects.get(id=id_votacao)
    
    if request.POST:
        form = OpcaoVotoForm(request.POST)
        if form.is_valid():
            opcao_voto = form.save(commit = False)
            opcao_voto.votacao = votacao
            opcao_voto.save()

            return redirect("votar", id_votacao)

    context = {
        "form": form,
    }

    return render(request, "votacao/opcao_voto/registrar_opcao.html", context)

def editar_opcao(request, id_opcao):
    obj_sala = get_object_or_404(SalaVotacao, id=id_sala)
    codigo = obj_sala.codigo
    usuario = request.user
    
    if request.POST:
        form = SalaVotacaoForm(request.POST, instance=obj_sala)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.codigo = codigo
            sala.admin = usuario
            sala.save()
            return redirect('listar_votacoes', obj_sala.id)
    else:
        form = SalaVotacaoForm(instance=obj_sala)
        
    context = {
        "form": form,
    }
    return render(request, 'votacao/sala/editar.html', context)

def listar_opcoes(request):
    opcoes = OpcaoVoto.objects.all()
    context = {
        "opcoes": opcoes,
    }
    return render(request, "votacao/opcao_voto/listar_opcoes.html", context)

def votar(request, id_votacao):
    pessoa = Usuario.objects.get(pk=request.user.id)
    votacao = Votacao.objects.get(pk=id_votacao)
    listOpcaoVoto = OpcaoVoto.objects.filter(votacao=votacao)

    if Pessoa_Voto.objects.filter(pessoa=pessoa, votacao=votacao) and votacao.voto_unico == True:
        messages.error(request,"O voto é unico!")
        return redirect("index") 

    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)
    
        try:
            voto = Pessoa_Voto.objects.get(votacao=votacao, pessoa=pessoa, opcao=objOpcaoVoto)
            
            objOpcaoVoto.numero_votos += 1
            objOpcaoVoto.save()
            
        except Pessoa_Voto.DoesNotExist:
            voto = Pessoa_Voto()
            
        voto.pessoa = pessoa
        voto.opcao = objOpcaoVoto
        voto.votacao = votacao
        voto.quantidade_votos +=1
            
        voto.save()
        
        return redirect('index')

    context = {
        "votacao": votacao,
        "listOpcaoVoto": listOpcaoVoto,
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

    opcoes = Pessoa_Voto.objects.filter(opcao=opcao)

    context = {
        "opcoes": opcoes,
    }

    return render(request, "administracao/detalhe_apuracao.html", context)
