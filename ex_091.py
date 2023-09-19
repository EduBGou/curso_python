from random import randint
from operator import itemgetter
# INPUTS
rslt = {'1° jogador': randint(1, 6),
        '2° jogador': randint(1, 6),
        '3° jogador': randint(1, 6),
        '4° jogador': randint(1, 6)}
# APRESENTAÇÃO
print('=' * 40)
print(f'{"- DESAFIO DOS DADOS -":^40}')
print('=' * 40)
# PRINT DOS RESULTADOS NOS DADOS
for i, v in enumerate(rslt.values()):
    print(f'O \033[33m{i + 1}° jogador\033[m tirou nos dados o número: \033[31m{v}\033[m')
print('=' * 40)
# RANKING DOS PLAYERS
ranking = sorted(rslt.items(), key=itemgetter(1), reverse=True)
print()

for i, v in enumerate(ranking):
    print(f'O \033[33m{v[0]}\033[m tirou \033[31m{v[1]}\033[m, ficando assim em \033[34m {i + 1}°\033[m Lugar.\n')
