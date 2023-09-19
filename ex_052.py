num = int(input('Digite um número inteiro: '))
boolPrimo = True

for i in range(2, num):
    isPrimo = num / i
    if isPrimo.is_integer():
        boolPrimo = False


if num == 1 or num == 0 or boolPrimo == False:
    print('{} não é um número primo.'.format(num))
else:
    print('{} é um número primo.'.format(num))