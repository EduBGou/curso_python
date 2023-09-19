mtz = []; pair = []; unp = []
spair = 0
sunp = 0
for i in range(0, 9):
    mtz.append(int(input(f'Digite o {i + 1}° valor: ')))
    if mtz[i] % 2 == 0 and mtz[i] != 0:
        pair.append(mtz[i])
        spair += mtz[i]
    elif mtz[i] % 2 != 0:
        unp.append(mtz[i])
        sunp += mtz[i]
lLarger = mtz[3]
if mtz[4] > lLarger:
    lLarger = mtz[4]
if mtz[5] > lLarger:
    lLarger = mtz[5]
print('-' * 30)
print(f'\n[{mtz[0]:^5}]  [{mtz[1]:^5}]  [{mtz[2]:^5}]')
print(f'\n[{mtz[3]:^5}]  [{mtz[4]:^5}]  [{mtz[5]:^5}]')
print(f'\n[{mtz[6]:^5}]  [{mtz[7]:^5}]  [{mtz[8]:^5}]\n')
print('-' * 30)
print(f'Estes são os números pares: {sorted(pair)}')
print(f'A soma dos números pares é: {spair}\n')
print(f'Estes são os números ímpares: {sorted(unp)}')
print(f'A soma dos números pares é: {sunp}\n')
print(f'A soma dos valores da 3° Coluna é: {mtz[2] + mtz[5] + mtz[8]}')
print(f'O maior valor da 2° Linha é: {lLarger}\n')
