from django import forms
from .models import *

class ContatoForm(forms.Form):
    nome = forms.CharField(label = '*Nome:', required = True)
    sobrenome = forms.CharField(label = '*Sobrenome:', required = True)
    email = forms.EmailField(label = '*Email:', required = True)
    titulo = forms.CharField(label = '*Título:', max_length = 50, required = True)
    messagem = forms.CharField(label = '*Messagem:', max_length = 500, required = True)

    class Meta:
        fields = ("__all__")

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório.",
                "invalid": "Insira um nome válido.",
            },
            "sobrenome":{
                "required": "O sobrenome é obrigatório.",
                "invalid": "Insira um sobrenome válido.",
            },
            "email":{
                "required": "O email é obrigatório.",
                "invalid": "Insira um email válido.",
            },
            "título":{
                "required": "O título é obrigatório.",
                "invalid": "Insira um título válido.",
            },
            "messagem":{
                "required": "O messagem é obrigatório.",
                "invalid": "Insira uma messagem válida.",
            },
        }