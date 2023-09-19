phrase = str(input('Digite uma frase: ')).strip().upper().split()
together = ''.join(phrase)
inverse = ''

for i in range(len(together) - 1, - 1, -1):
    inverse += together[i]
'''
OU,
inverse = together[::-1]
'''

print('o inverso de {} é {}.'.format(together, inverse))
if together == inverse:
    print('Esta frase é um políndromo.')
else:
    print('Esta frase é não é um políndromo.')