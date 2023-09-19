from random import randint
from time import sleep
numList = []

ans = int(input('\nQuantos sorteios de palpites você deseja? '))
print('=' * 60)
print(f'{"---> MEGA SENA <---":^60}')
print('=' * 60)
for c in range(1, ans + 1):
    i = 0
    while i < 6:
        num = randint(1, 60)
        if num not in numList:
            numList.append(num)
            i += 1
    sleep(0.3)
    print(f'Esse foi o {c}° palpite: {numList}')
    numList.clear()
sleep(0.5)
print('=' * 60, f'\n{"BOA SORTE!!!":^60}\n')