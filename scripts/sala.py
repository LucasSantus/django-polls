from votacao.models import *

'''
CÓDIGO PARA EXECUTAR O SCRIPT
python manage.py shell
exec(open('scripts/sala.py').read())
'''

escolha = 1

def registrar_salas():
    qtd = int(input("\nInsira a quantidade de registros: "))

    usuario = Usuario.objects.get(email="admin@admin.com")
    for contador in range(qtd):
        try:
            sala = SalaVotacao()
            sala.titulo = Votacao.generated_code_random()
            sala.codigo = Votacao.generated_code_random()
            sala.admin = usuario
            sala.save()
            sala.usuarios.add(usuario)
            print(f'{contador+1}º Sala [{sala.titulo}] foi cadastrada com sucesso!')
        except:
            print(f'Falha ao realizar o cadastro da sala de votação!')

def deletar_salas():
    SalaVotacao.objects.all().delete()
    print("Todas as salas de votações foram deletadas com sucesso!")

while escolha != 0:
    print("\n----- Number 1 - Registrar Salas -----")
    print("\n----- Number 2 - Deletar Salas   -----")
    print("\n----- Number 0 - SAIR            -----")
    
    escolha = int(input("\nInsira uma Opção:"))
    
    if escolha == 1:
        registrar_salas()
    elif escolha == 2:
        deletar_salas()
    elif escolha == 0:
        print("Volte sempre!")
    else: 
        print("Opção Inválida!")