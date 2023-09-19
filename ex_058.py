from random import randint

print('Este é o jogo da adivinhação, tente descobrir o valor entre 0 e 10 que o Computador escolheu.')
won = 0
pcChoice = randint(0, 10)

while won == 0:
    userChoice = int(input('\nDigite um número entre 0 e 10: '))

    if 0 <= userChoice <= 10:

        if userChoice == pcChoice:
            print('Você acertou o número escolhido pelo computador!')
            won = 1

            while won == 1:
                pAgain = str(input('\nDeseja jogar mais uma rodada? ')).strip().upper()
                
                if pAgain == 'S':
                    won = 0
                    pcChoice = randint(0, 10)
                elif pAgain == 'N':
                    won = 2
                else:
                    print('Digite apenas "S" para sim, ou "N" para não.')

        elif userChoice < pcChoice:
            print('Mais (+)... Tente novamente.')
        elif userChoice > pcChoice:
            print('Menos (-)... Tente novamente.')
        else:
            print('Você errou o número escolhido pelo computador.')

    else:
        print('O valor digitado não se encontra entre 0 e 10.')
