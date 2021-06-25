from django import forms
from cadastro.models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "O nome completo da pessoa é obrigatório para o registro",
            },

            "cpf":{
                "required": "O  cpf da pessoa é obrigatório para o registro",
                "invalid": "Por favor, insira um CPF válido!",
            },

            "data_nascimento":{
                "required": "A data de nascimento da pessoa é obrigatório para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/DD/AAAA)",
            },

            "email":{
                "required": "Por favor, informe o número da casa a ser visitada",
                "invalid": "Por favor, informe um formato válido para o email",
            },
        }
