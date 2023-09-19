value = []
for i in range(0, 5):
    value.append(int(input('Digite um valor: ')))
    if i == 0:
        larger = less = value[i]
    elif value[i] > larger:
        larger = value[i]
    elif value[i] < less:
        less = value[i]
for c, i in enumerate(value):
    print(f'Você digitou na posição {c}, o número: \033[0;33m{i}\033[m.')
print(f'O maior valor é {larger}, na posição {value.index(larger)}, o menor é {less} na posição {value.index(less)}.')