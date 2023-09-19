totalCost = overItens = 0

while True:
    nameItem = str(input('Digite o nome do item: ')).strip().capitalize()
    priceItem = float(input('Quanto ele custa? R$ '))
    if totalCost == 0:
        cheapName = nameItem
        cheapPrice = priceItem
    elif priceItem < cheapPrice:
        cheapName = nameItem
        cheapPrice = priceItem
    totalCost += priceItem
    if priceItem > 1000:
        overItens += 1
    ask = ' '
    while ask not in 'SN':
        ask = input('Deseja inserir mais um item à compra? (Digite [N] caso Não): ').strip().upper() [0]
    if ask == 'N':
        break
print(f'- O valor total da compra é de R$ {totalCost:.2f}; \n- Há {overItens} itens acima de R$ 1000; \n- O produto mais barato foi {cheapName}, por R$ {cheapPrice:.2f};')
print('Volte Sempre!')