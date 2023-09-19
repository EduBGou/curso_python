
value = 0
while value >= 0:
    value = int(input("A tabuada de qual número deseja descobrir? "))
    if value <= 0:
        break
    rept = int(input('Qual o limite da Tabuada? '))
    if rept <= 0:
        break
    soluction = 0

    print(f'Aqui está a Tabuada de {value}, {rept} vezes! \n')
    i = 1
    while (i <= rept):
        soluction = value * i
        print(f'{value} x {i} = {soluction} \n')
        i += 1
print('Programa encerrado, volte sempre!')
