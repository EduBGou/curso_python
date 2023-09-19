value = int(input('Digite o N° que deseja saber o Fatorial: '))
expo = 1

for i in range(1, value + 1):
    expo = expo * i

result =  expo
print('O Fatorial de {} é = {}'.format(value, result))