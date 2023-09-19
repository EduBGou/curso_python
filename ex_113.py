def canBeFloat(value):
    try:
        value = float(value)
        return True
    except (ValueError, TypeError):
        return False
     
while True:
    vInt = str(input('Digite um número inteiro: ')).strip()
    if vInt.isnumeric():
        vInt = int(vInt)
        break
    else:
        print('Digite um número inteiro válido.')

while True:
    vFloat = str(input('Digite um número real: ')).strip().replace(',', '.')
    if canBeFloat(vFloat):
        vFloat = float(vFloat)
        break
    else:
        print('Digite um número real válido.')

print(f'Você digitou i inteiro {vInt} e o float {vFloat}')