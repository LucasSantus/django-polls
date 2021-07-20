from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ('__all__')

        error_messages = {
            "nome":{
                "required": "O nome completo da pessoa é obrigatório para o registro",
                "invalid": "Por favor, insira um CPF válido!",
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
