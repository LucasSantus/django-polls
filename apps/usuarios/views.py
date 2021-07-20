from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
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
    print(data["is_email_registered"])
    if not data['is_email_registered']:
        data['error_message'] = 'Este e-mail não está cadastrado no sistema!'
    return JsonResponse(data)

def edit_user(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            return redirect('post_detail', pk=user.pk)
    else:
        form = UsuarioForm(instance=user)
    context = {
        "form": form,
    }
    return render(request, 'administracao/post_edit.html', context)
