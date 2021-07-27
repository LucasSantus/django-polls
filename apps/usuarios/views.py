from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

def registrar_pessoa(request):
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            pessoa.save()
            
            messages.success(
                request, "Pessoa registrado com sucesso!"
            )
            
            return redirect("listar_pessoas")

    context = {
        "nome_pagina": "Registrar pessoa",
        "form": form,
    }

    return render(request, "usuarios/registrar_pessoa.html", context)

def listar_pessoas(request):
    usuarios = Usuario.objects.all()
    context = {
        "pessoas": usuarios,
    }
    return render(request, "usuarios/listar_pessoas.html", context)

def perfil_usuario(request):
    usuario = Usuario.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm(instance=usuario)
    
    context = {
        'form': form,
    }
    return render(request, "usuarios/perfil_usuario.html", context)
