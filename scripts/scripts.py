from votacao.models import *

# import uuid

import string
import random

# CÓDIGO PARA EXECUTAR O SCRIPT
# python manage.py shell
# exec(open('scripts/scripts.py').read())

def code_generated(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def code():
    codigo = code_generated()
    valid = True
    while valid == True:
        try:
            SalaVotacao.objects.get(codigo=codigo)
            codigo = code_generated()
        except SalaVotacao.DoesNotExist:
            valid = False
            return codigo
