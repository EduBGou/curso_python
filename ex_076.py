listItens = ['Ryzen 5 5600g ', 650.00, 
              'GTX 1660', 1460.00,
              'DDR4 - Mem. RAM 8Gb, 3200MHz ', 110.00,
              'DDR4 - Mem. RAM 8Gb, 3200MHz ', 110.00,
              'Monitor Full HD 144Hz ', 800.00]
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
