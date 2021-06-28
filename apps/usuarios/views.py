from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

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
    pessoas = Pessoa.objects.all()
    context = {
        "pessoas": pessoas,
    }
    return render(request, "usuarios/listar_pessoas.html", context)

def perfil_usuario(request):
    pessoa = Pessoa.objects.get(id=1)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm(instance=pessoa)
    
    context = {
        'form': form,
    }

    return render(request, "usuarios/perfil_usuario.html", context)
