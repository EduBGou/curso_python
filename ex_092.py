from datetime import datetime

# INPUTS
info = {}
info['name'] = str(input('Digite o seu nome: ').capitalize().strip())
born = int(input('Digite o seu ano de nascimento: '))
info['age'] = datetime.now().year - born
info['workCard'] = int(input('N° da Carteira de Trabalho (0 se não tiver): '))

# ADDTIONAL INPUTS
if info['workCard'] != 0:
    info['hiringYear'] = int(input('Digite em que ano foi contratado: '))
    info['wage'] = int(input('Digite o valor do seu salário: R$ '))
    contribution = datetime.now().year - info['hiringYear']
    print('=' * 50)
else:
    print('=' * 50)
    print('Como não possui carteira de trabalho, \nnão terá acesso as informações relaconadas.')
    print('=' * 50)

# PRINTS
print('\033[35mEstas são as informações registradas:\033[m')
print(f'    Nome ................... {info["name"]}')
print(f'    Idade .................. {info["age"]}')
if info['workCard'] != 0:
    print(f'    Carteira de Trabalho ... {info["workCard"]}')
    print(f'    Ano de Contratação ..... {info["hiringYear"]}')
    print(f'    Anos de Contribuição ... {contribution}')
    print(f'    Salário ................ R$ {info["wage"]}')
print()
if info['workCard'] != 0 and contribution >= 35:
    print(f'Você já pode se aposentar, pois possui {contribution} de 35 anos anos de contribuição mínima.')
elif info['workCard'] != 0 and contribution < 35:
    print(f'Você ainda não pode se aposentar, pois possui {contribution} de 35 anos anos de contribuição mínima. Ou seja, faltam {info["age"] - contribution} anos para receber a sua aposentadoria (quanto tiver {info["age"] - contribution + 35} anos de idade).')
