from django.contrib import admin
from cadastro.models import * 

admin.site.register(Pessoa)
admin.site.register(Votacao)
admin.site.register(OpcaoVoto)