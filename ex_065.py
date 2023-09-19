#INPUTS
again = True
rept = 0
sumTotal = 0
larger = 0
less = 0

#LOOP
while again:
    num = int(input('Digite um número: '))
    if rept == 0:
        larger = num
        less = num
    elif rept >= 0:
        if num > larger:
            larger = num
        if num < less:
            less = num
    sumTotal += num
    rept += 1
    ask = str(input('Quer continuar? (N = Não): ')).strip().upper() [0]
    if ask == 'N':
        again = False

#PRINTS
med = sumTotal / rept
print('Você digitou {} números, e a média é {}.'.format(rept, med))
print('O maior número é {}, enquanto o menor é {}'.format(larger, less))