from django.shortcuts import render
from .models import Pessoa

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
