from datetime import date

people = 0
numMajority = 0

for i in range(0, 7):
    born = int(input('Digite o ano da data de nascimento da {}° pessoa: '.format(i + 1)))
    age = date.today().year - born

    #VERIFICAÇÃO DA IDADE
    if age >= 21:
        numMajority += 1
        print('A {}° pessoa atingiu a maioridade, pois possui {} anos.\n'.format(i + 1, age))

    elif age == 0:
        print('A {}° não pessoa atingiu a maioridade, pois nasceu este ano.\n'.format(i + 1))

    elif age < 0:
        print('Esta pessoa não nasceu ainda, ainda faltam {} anos para ela nascer.\n'.format(age * (- 1)))

    else:
        print('A {}° pessoa não atingiu a maioridade, pois possui apenas {} anos.\n'.format(i + 1, age))

print('Ao todo, {} pessoas já atingiram a maioridade e {} ainda não.'.format(numMajority, (i + 1) - numMajority))