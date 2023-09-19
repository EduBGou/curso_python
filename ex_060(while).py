value = int(input('Digite o N° que deseja saber o Fatorial: '))
expo = 1
i = value
while i > 0:
    expo = expo * i
    i -= 1
result =  expo
print('O Fatorial de {} é = {}'.format(value, result))