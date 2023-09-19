#SORTEIA 5 NÚMEROS E MOSTRA O MAIOR E O MENOR
from random import randint
sortition = (
        (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)),
        (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10))
        )
amount = int(input('Quantos números quer que sejam gerados? (limite = 10): '))
print(f'Esses são os números sorteados: {sortition[0:amount]}')
print(f'O maior número é: {max(sortition[0:amount])}.')
print(f'O menor número é: {min(sortition[0:amount])}.')