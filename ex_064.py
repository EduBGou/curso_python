total = 0
n = 0
rept = 0
while n != 999:
    n = int(input('DIgite um número (999 para parar): '))
    total += n
    rept += 1
total -= 999
if n == 999:
    print('Você digitou {} números diferentes, sendo a soma deles de {}.'.format(rept, total))