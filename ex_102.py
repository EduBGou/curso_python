def fFactorial(n, show=False):
    """
    -> Descobre o fatorial de um número
    :param n = número a ser fatorado.
    :param show = (opcional) Exibe o cálculo.
    :retur = fatorial do número.
    """
    total = 1
    for i in range(1, n + 1):
        total *= i
        if show == True:
            if i == n:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    return total

num = int(input('Fatorial: '))
show = bool(input('Deseja que seja exibido? (Digite "ENTER" p/ "NÃO"): '))

print('=' * 45)
print(fFactorial(num, show))
print('=' * 45)
help(fFactorial)