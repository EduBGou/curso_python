def counter(start, end, step):
    print(f'Contagem de {start} até {end} de {step} em {step}:')
    if start > end:
        if step > 0:
            step *= -1
        end -= 1
    elif start < end:
        if step < 0:
            step *= -1
        end += 1
    for i in range(start, end, step):
        print(i, end=' ')
    print()
    print('=' * 30)
counter(1, 10, 1)
counter(10, 0, 2)

s = int(input('Digite o Início: '))
while True:
    e = int(input('Digite o Fim: '))
    if s != e:
        break
    print('O Início e o Fim não podem ser o mesmo valor.\n')

while True:
    stp = int(input('Digite o Passo: '))
    if stp != 0:
        break
    print('O Número 0 não é aceito.\n')

counter(s, e, stp)
