from django import forms
from .models import *

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = ('__all__')

        error_messages = {
            "titulo":{
                "required": "O nome é obrigatório para o registro",
                "invalid": "oi",
                'blank' : 'preenche isso aí seu bosta'
            },

            "descricao":{
                "required": "a descrição é obrigatório para o registro",
            },

            "anonimo":{
                "required": "A data de nascimento da pessoa é obrigatório para o registro",
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

class SalaVotacaoForm(forms.ModelForm):
    class Meta:
        model = SalaVotacao
        fields = ('__all__')

class OpcaoVotoForm(forms.ModelForm):
    class Meta:
        model = OpcaoVoto
        fields = ('__all__')
