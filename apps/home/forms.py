from django import forms
from .models import *

class ContatoForm(forms.ModelForm):
    nome = forms.CharField(label = '')
    sobrenome = forms.CharField(label = '')
    email = forms.CharField(label = '')
    titulo = forms.CharField(label = '')
    messagem = forms.CharField(label = '')

    class Meta:
        fields = ("__all__")

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': '*Nome:'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': '*Sobrenome:'}),
            'email': forms.EmailInput(attrs={'placeholder': '*Email:'}),
            'titulo': forms.TextInput(attrs={'placeholder': '*Título:'}),
            'messagem': forms.TextInput(attrs={'placeholder': '*Messagem:'}),
        }

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório.",
                "invalid": "Insira um nome válido.",
                "blank" : "É necessário inserir um nome."
            },
            "sobrenome":{
                "required": "O sobrenome é obrigatório.",
                "invalid": "Insira um sobrenome válido.",
                "blank" : "É necessário inserir um sobrenome."
            },
            "email":{
                "required": "O email é obrigatório.",
                "invalid": "Insira um email válido.",
                "blank" : "É necessário inserir um email."
            },
            "título":{
                "required": "O título é obrigatório.",
                "invalid": "Insira um título válido.",
                "blank" : "É necessário inserir um título."
            },
            "messagem":{
                "required": "O messagem é obrigatório.",
                "invalid": "Insira um messagem válido.",
                "blank" : "É necessário inserir um messagem."
            },
        }

        # labels = {
        #     'first_name': '',
        #     'last_name': '',
        #     'email': '',
        #     'username': '',
        # }
