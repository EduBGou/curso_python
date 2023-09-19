from lib.interface import *
from lib.file import *

def fOption(msg):
    while True:
        try:
            opt = int(input(f'\033[0;33m{msg}\033[m '))
            if 0 < opt < 4:
                return opt
            else:
                print('Insira um valor válido.')
        except:
            print('Insira o número da opção corretamente.')

# INITIAL DECLARATIONS
user = {}
file = 'allUserFile.txt'

if fileExist(file):
    print('Arquivo encontrado com sucesso!')
else: 
    print('Não encontramos o arquivo!')
    try:
        createFile(file)
        print('Criamos o arquivo.')
    except:
        print('Problema ao criar o arquivo.')

# PROGRAM
while True:
    fMenu('Ver usuários cadastrados.', 'Cadastrar um novo usuário.', 'Sair do Programa.')
    option = fOption('Digite a opção:')

    # MOSTRAR A LISTA GERAL
    if option == 1:
        readFile(file)
    
    # ADICIONAR À LISTA GERAL
    if option == 2:
        user['name'] = str(input('Digite o nome: ').capitalize().strip())
        while True:
            try:
                user['age'] = int(input('Digite a idade: '))
                break
            except:
                print('Insira uma idade válida.')
    
        register(file, user['name'], user['age'])

    # SAIR DO PROGRAMA
    if option == 3:
        break

print('Programa Finalizado com Sucesso!')