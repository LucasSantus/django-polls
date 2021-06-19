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

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = ('nome', 'descricao','anonimo', 'voto_unico', 'data_inicio', 'data_fim', )

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para o registro",
            },

            "descricao":{
                "required": "a descrição é obrigatório para o registro",
            },

            "anonimo":{
                "required": "A data de nascimento da pessoa é obrigatório para o registro",
            },

            "voto_unico":{
                "required": "Por favor, informe o número da casa a ser visitada",
            },
            "data_inicio":{
                "required": "O  cpf da pessoa é obrigatório para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/DD/AAAA)",
            },

            "data_fim":{
                "required": "A data de nascimento da pessoa é obrigatório para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/DD/AAAA)",
            },
        }

class OpcaoVotoForm(forms.ModelForm):
    class Meta:
        model = OpcaoVoto
        fields = ('__all__')