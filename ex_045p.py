import random

def jogo(ptsuser, ptspc):

    # Apresenta o placar
    print('\nPLACAR: USUÁRIO > {}\n        COMPUTADOR > {}'.format(ptsuser, ptspc))
    print('\033[0;37m=\033[m' * 80)

    # Escolha PC e usuário
    escolhapc = int(random.randint(1, 3))
    escolhauser = int(input('''Escolha uma das opções abaixo, eu já escolhi a minha...
    [1] - PEDRA
    [2] - PAPEL
    [3] - TESOURA
    R: '''))

    # Testa se usúário escolheu opção válida
    if escolhauser < 1 or escolhauser > 3:
        print('\nPreste atenção seu bizonho!!! Escolha uma opção válida [1, 2 ou 3].')
        jogo(ptsuser, ptspc)

    else:
        # Atribuições de string à escolha do usuário:
        if escolhauser == 1:
            escolhausernome = str('PEDRA')
        elif escolhauser == 2:
            escolhausernome = str('PAPEL')
        else:
            escolhausernome = str('TESOURA')

        # Atribuições de string à escolha do PC:
        if escolhapc == 1:
            escolhapcnome = str('PEDRA')
        elif escolhapc == 2:
            escolhapcnome = str('PAPEL')
        else:
            escolhapcnome = str('TESOURA')

        # Resultado de empate
        if escolhauser == escolhapc:
            print('\n\033[1;33mEmpatamos essa, nós dois escolhemos {}! Ninguém pontua.\033[m'.format(escolhausernome))
            jogo(ptsuser, ptspc)

        else:
            # Ver quem ganha
            if (escolhauser == 1 and escolhapc == 2) or (escolhauser == 2 and escolhapc == 3) or (escolhauser == 3 and escolhapc == 1):
                print('\n\033[1;31mPerdeu Mané!Eu escolhi {}, que ganha de {}.\033[m'.format(escolhapcnome, escolhausernome))
                ptspc = ptspc + 1
                jogo(ptsuser, ptspc)
            else:
                print('\n\033[1;32mVocê ganhou! Eu escolhi {} que perde de {}.\033[m'.format(escolhapcnome, escolhausernome))
                ptsuser = ptsuser + 1
                jogo(ptsuser, ptspc)


# Cabeçário do jogo com 70 '=' menos título colorido (centralizado)
print('{:=^90}'.format(' \033[1;33mJOGO: PEDRA, PAPEL E TESOURA\033[m '))

jogar = int(input('Quer jogar uma partida? (Se SIM digite 1): '))
if jogar == 1:
    jogo(ptsuser=0, ptspc=0)