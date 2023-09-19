infoDic = {}; infoList = []
sumAge = amtFem = 0

while True:
    # INPUTS
    infoDic.clear()
    infoDic['name'] = str(input('\nNome: ').capitalize().strip())
    infoDic['age'] = int(input('Idade: ').capitalize().strip())
    sumAge += infoDic['age']
    while True:
        infoDic['sex'] = str(input('Sexo (M/F): ')).upper()
        if infoDic['sex'] in 'MF':
            if infoDic['sex'] in 'F':
                amtFem += 1
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    # ADD DIC IN LIST
    infoList.append(infoDic.copy())
    # ASK FOR CONTINUE
    ask = str(input('Deseja continuar? (N para "Não"): ').upper())
    if ask == 'N':
        break

# CALCULATING AVERAGE
average = sumAge / len(infoList)

# PRINTS
print(f'\nA) Ao todo temos {len(infoList)} pessoas cadastradas.')
print(f'B) A média da idade é de {average:3.1f} anos.')
if amtFem > 0:
    print(f'C) Há {amtFem} mulher(es) cadastrada(s), sendo ela(s): ', end='')
    # VERIFLY SEX
    for c, p in enumerate(infoList):
        if p['sex'] in 'F':
            if c == len(infoList) - 1:
                print(f'{p["name"]}', end='.\n')
            else:
                print(f'{p["name"]}', end=', ')
else:
    print('C) Não há mulheres cadastradas.')
if len(infoList) == 0:
    print('D) Não há pessoas o suficiente para mostrar quais que estão acima da média.')
else:
    print('D) Lista de pessoas acima da idade média: ')
    for p in infoList:
        if p['age'] > average:
            print(f'- {p["name"]} com {p["age"]} anos.')