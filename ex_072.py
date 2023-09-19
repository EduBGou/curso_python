# DIGITAR UM NÚMERO DE 0 À 10 E PRINTAR ELES EM EXTENSO
num = -1
extNum = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while 0 >num or num > 10:
    num = int(input('Digite um número de 0 à 10: '))
print(extNum[num])