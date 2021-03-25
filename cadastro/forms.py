from django import forms
from cadastro.models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            "nome", "cpf", "data_nascimento", "email",
        ]  
        error_messages = {
            "nome":{
                "required": "O nome completo da pessoa é obrigatório para o registro",
            },

            "cpf":{
                "required": "O  cpf da pessoa é obrigatório para o registro",
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
