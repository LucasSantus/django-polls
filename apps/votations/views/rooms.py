from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from votations.forms import RoomForm

def create_room(request):
    form = RoomForm()

    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            sala = form.save(commit = False)
            sala.codigo = Votation.generated_code_random()
            sala.admin = request.user
            sala.save()
            sala.usuarios.add(request.user)
            messages.success(request,"Sala de Votação registrada com sucesso!")
            return redirect("index")

    context = {
        "teste": "teste",
        "form": form,
        # "usuario": request.user,
        # "modal": {
        #     "title": "Retornar para Sala de Votações",
        #     "content": "Deseja realmente continuar com essa ação?",
        #     "url": "index",
        # },
    }

    return render(request, "votations/rooms/create_room.html", context)

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
        "modal": {
            "title": "Retornar para Sala de Votações",
            "content": "Deseja realmente continuar com essa ação?",
            "url": "index",
        }
    }

    return render(request, 'votacao/sala/editar.html', context)

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
    
    context = {
        "modal": {
            "title": "Retornar para Sala de Votações",
            "content": "Deseja realmente continuar com essa ação?",
            "url": "index",
        }
    }

    return render(request, "votacao/sala/conectar.html", context)
