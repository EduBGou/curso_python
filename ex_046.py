value = float(input("A tabuada de qual número deseja descobrir? "))
rept = int(input('Qual o limite da Tabuada? '))
soluction = 0

print('Aqui está a Tabuada de {}, {} vezes! \n'.format(value, rept))

for i in range(1, rept + 1):
    soluction = value * i
    print('{} x {} = {} \n'.format(value, i, soluction))
#