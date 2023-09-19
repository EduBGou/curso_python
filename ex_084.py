datas = []; people = []
big = sma = 0
bigName = []; smaName = []

while True:
    datas.append(str(input('\nDigite o nome: ')).strip().capitalize())
    datas.append(float(input('Digite a massa corporal: ')))

    # DESCOBRINDO O MENOR OU MAIOR
    if len(people) == 0:
        big = sma = datas[1]
    else:
        if datas[1] > big:
            big = datas[1]
        if datas[1] < sma:
            sma = datas[1]
    
    people.append(datas[:])
    datas.clear()
    ask = str(input('\nQuer continuar? (apenas "N" para não): ')).upper()
    if ask == 'N':
        break

# ADICIONA OS NOMES REFERENTE À big E sma EM UMA LISTA
for i in people:
    if i[1] == big:
        bigName.append(i[0])
    elif i[1] == sma:
        smaName.append(i[0])

# PRINTS
print('=' * 50)
print(f'\nO número de pessoas cadrastadas é de {len(people)}.')
print(f'A maior massa corporal registrada é de {big:.2f}Kg, de: {bigName}.')
print(f'A menor massa corporal registrada é de {sma:.2f}Kg, de: {smaName}.')
