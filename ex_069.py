minors = womanMinors = amountMan = 0
while True:
    age = int(input('Digite a idade da pessoa: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper() [0]
    if age < 18:
        minors += 1
    if sex == 'M':
        amountMan += 1
    if age < 20 and sex == 'F':
        womanMinors += 1
    cntn = input('Deseja inserir mais uma pessoa? (Digite "N" para sair): ').strip().upper()
    if cntn == 'N':
        break
print(f'O número de: \n- Pessoas com menos de 18 anos: {minors}; \n- Homens: {amountMan}; \n- Mulheres com menos de 20 anos: {womanMinors};')
