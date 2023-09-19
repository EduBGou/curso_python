from curso_python.ex_109.cursoemvid import coin

value = float(input('\nDigite o valor: R$ '))
show = bool(input('Deseja ser mostrado "R$"? ("ENTER" p/ "não"): '))
print(f'\nO dobro de {value:.2f} é: {coin.double(value, show=show)}')
print(f'A metade de {value:.2f} é: {coin.half(value, show=show)}')
prct = int(input('\nEscolha a porcentagem para aumentar: '))
print(f'Aumentando em {prct}% de {value:.2f}, temos: {coin.increase(value, prct, show=show)}')
prct = int(input('\nEscolha a porcentagem para diminuir: '))
print(f'Reduzindo em {prct}% de {value:.2f}, temos: {coin.decrease(value, prct, show=show)}\n')