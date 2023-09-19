from random import randint
from time import sleep
lst = []
def prize(l):
    print('\nSorteando 5 números: ', end='')
    for i in range(0, 5):
        l.append(randint(0, 20))
        print(f'{l[i]}', end=' ', flush=True)
        sleep(0.5)
    print()
def sumPairs(l):
    total = 0
    for i in l:
        if i % 2 == 0:
            total += i
    print(f'O total da soma dos números pares do sorteio é: {total}.\n')
prize(lst)
sumPairs(lst)
