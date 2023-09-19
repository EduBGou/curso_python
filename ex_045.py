from random import choice

#QUANDO O USER PERDE
def pnts_lose(uChoice, pcChoice, uPnts,pcPnts): 

    print('Você \033[0;31mperdeu\033[m esta partida! Pois a minha escolha que foi {} ganha de {}.'.format(pcChoice, uChoice))
    pcPnts += 1
    print('\033[0;36mSua Pontuação: {} --- Minha Pontuação: {}\033[m'.format(uPnts, pcPnts))
    game(uPnts, pcPnts)

#QUANDO O USER GANHA
def pnts_won(uChoice, pcChoice, uPnts,pcPnts): 

    print('Você \033[0;32mganhou\033[m esta partida! Pois {} ganha de {}, que foi a minha escolha.'.format(uChoice, pcChoice))
    uPnts += 1
    print('\033[0;36mSua Pontuação: {} --- Minha Pontuação: {}\033[m'.format(uPnts, pcPnts))
    game(uPnts, pcPnts)

#EXIBIÇÃO DOS RESULTADOS E PONTUAÇÃO
def endgame(arg_pe, arg_pa, arg_te, uChoice, pcChoice, uPnts, pcPnts):
        if uChoice == pcChoice:
            print('\033[0;33mEmpatamos!\033[m nós dois escolhemos {}.'.format(uChoice))
            print('Sua Pontuação: {} --- Minha Pontuação: {}'.format(uPnts, pcPnts))
            game(uPnts, pcPnts)

        elif uChoice == arg_pe:
                if pcChoice == arg_pa:
                    pnts_lose(uChoice, pcChoice, uPnts,pcPnts)
                else:
                    pnts_won(uChoice, pcChoice, uPnts,pcPnts)

        elif uChoice == arg_pa:
                if pcChoice == arg_te:
                    pnts_lose(uChoice, pcChoice, uPnts,pcPnts)
                else:
                    pnts_won(uChoice, pcChoice, uPnts,pcPnts)

        elif uChoice == arg_te:
                if pcChoice == arg_pe:
                    pnts_lose(uChoice, pcChoice, uPnts,pcPnts)

                else:
                    pnts_won(uChoice, pcChoice, uPnts,pcPnts)

#JOGO
def game(uPnts, pcPnts):

    #APRESENTAÇÃO
    print('-' * 60)
    print ('Vamos ver quem de nós dois vence em uma partida de \033[0;34mJokenpô!\033[m')

    #INPUTS
    nameChoices = ['PEDRA', 'PAPEL', 'TESOURA']
    uChoice = str(input('\n- {}; \n- {}; \n- {}; \n\nDigite sua escolha: '.format(nameChoices[0], nameChoices[1], nameChoices[2]))).upper().strip()
    pcChoice = choice(nameChoices)

    #VERIFICAÇÃO DO RESULTADO
    if uChoice != nameChoices[0] and uChoice != nameChoices[1] and uChoice != nameChoices[2]:
        print('Você precisa digitar o nome corretamente.')
        game(uPnts, pcPnts)
    else:
       endgame(nameChoices[0], nameChoices[1], nameChoices[2], uChoice, pcChoice, uPnts, pcPnts)

#COMEÇAR TUDO
game(uPnts=0, pcPnts=0)