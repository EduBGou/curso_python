value = []
while True:
    value.append(int(input('\nDigite um valor: ')))
    if value[-1] in value[:-1]:
        value.pop()
        print('Valores iguais não são armazenados.')
    ask = input('Quer continuar? (Se não, digite "N"): ').upper()
    if ask == 'N':
        break
print(f'Esta é a sua lista de valores: {sorted(value)}')