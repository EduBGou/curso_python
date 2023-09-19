from random import randint
print('JOGO: IMPER ou PAR\n')
wins = 0
while True:
    pcNum = randint(0, 20)
    userNum = int(input('Digite seu número: '))
    userChoice = ''
    while userChoice not in 'PI':
        userChoice = str(input('Você escolhe ser Imper ou Par? (I/P): ')).strip().upper() [0]
    total = userNum + pcNum
    if total % 2 == 0:
        totalChoice = 'P'
    else:
        totalChoice = 'I'
    if userChoice == totalChoice:
        wins += 1
        print(f'''Parabéns, você venceu!
O Computador escolheu {pcNum} e você {userNum}, totalizando em {total}''')
        print(f'Você possui {wins} vitórias.\n')
    else:
        print(f'''Você perdeu!
O Computador escolheu {pcNum} e você {userNum}, totalizando em {total}\n''')
        break
print(f'O jogo acabou! Você acumulou {wins} vitória(s) até sua derrota.')