def summary(value, amt):
    return f'''
Valor Analizado:            R$ {value:.2f}
Mudança de Porcentagem:     R$ {value * ( 1 + (amt / 100)):.2f}
Dobro do Valor:             R$ {value * 2:.2f}
Metade do Valor:            R$ {value / 2:.2f}'''

val = float(input('\nDigite o valor: R$ '))
prct = int(input('Escolha a porcentagem para aumentar(+) ou diminuir(-): '))
print(summary(val, prct), '\n')