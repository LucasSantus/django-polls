from votacao.models import *

'''
CÓDIGO PARA EXECUTAR O SCRIPT
python manage.py shell
exec(open('scripts/sala.py').read())
'''

def registrar_salas():
    print("\n")
    qtd = int(input("Insira a Quantidade de Salas para Registrar:"))

    usuario = Usuario.objects.get(email="admin@admin.com")
    for contador in range(qtd):
        try:
            sala = SalaVotacao()
            sala.titulo = Votacao.generated_code_random()
            sala.codigo = Votacao.generated_code_random()
            sala.admin = usuario
            sala.save()
            sala.usuarios.add(usuario)
            print(f'{contador+1}º Sala {sala.titulo} cadastrada com sucesso!')
        except:
            print(f'Erro ao tentar cadastrar sala!')

def deletar_salas():
    SalaVotacao.objects.all().delete()
    print("Todas as Salas foram deletadas com sucesso!")

escolha = 1

while escolha != 0:
    print("\n ----- Number 1 - Registrar Salas -----")
    print("\n ----- Number 2 - Deletar Salas   -----")
    print("\n ----- Number 0 - SAIR            -----")
    escolha = int(input("Insira uma Opção:"))
    if escolha == 1:
        registrar_salas()
    elif escolha == 2:
        deletar_salas()
    else: 
        print("Opção Inválida!")