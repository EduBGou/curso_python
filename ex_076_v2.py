i = 1
listItens = [' ']
while i > 0:
    listItens.append(str(input(f'Nome do Ítem {i}: ')) + ' ')

    listItens.append(int(input(f'Valor do Ítem {i}: R$ ')))
    if ' ' in listItens:
        listItens.remove(' ')
    ask = str(input('Digite "N" se quiser parar de adicionar ítens: ')).strip().upper()
    if ask == 'N':
        i = -1
    i += 1
print('=' * 50)
total = 0
for i in range(0, len(listItens)):
    # NAME
    if i % 2 == 0: 
        print(f'{listItens[i]:-<35}', end = ' ')
    # PRICE
    else: 
        print(f'R$ {listItens[i]:.2f}')
        total += listItens[i]
print('=' * 50)
print(f'O total da compra foi de R$ {total:.2f}')
print('=' * 50)
