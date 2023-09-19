tuplaNum = (int(input('Digite um número: ')), int(input('Digite um número: ')), 
            int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O número 9 apareceu {tuplaNum.count(9)} vezes.')
if 3 in tuplaNum:
    print(f'O número 3 teve sua primeira aparição na {tuplaNum.index(3) + 1}° colocação (desconsiderando a 0).')
else:
    print('Não há o número 3 na tupla')
print(f'Esses são os números pares encontrados: ', end = '')
for i in range(0, len(tuplaNum)):
    if i == len(tuplaNum) - 1:
        if tuplaNum[i] % 2 == 0:
            print(tuplaNum[i])
    else:
        if tuplaNum[i] % 2 == 0:
            print(tuplaNum[i], end = ', ')