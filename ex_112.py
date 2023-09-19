def summary(value, amt):
    return f'''
Valor Analizado:            R$ {value:.2f}
Mudança de Porcentagem:     R$ {value * ( 1 + (amt / 100)):.2f}
Dobro do Valor:             R$ {value * 2:.2f}
Metade do Valor:            R$ {value / 2:.2f}'''

while True:
    val = str(input('Digite o valor: R$ ').strip())
    if val.isalpha():
        print('ERRO! Insira um valor válido.')
    else:
        val = float(val)
        break
while True:
    prct = str(input('Escolha a porcentagem para aumentar(+) ou diminuir(-): '))
    if prct.isalpha():
        print('ERRO! Insira um valor válido.')
    else:
        prct = int(prct)
        break
print('=' * 40)
print(f'{"RESUMO DE VALORES":^40} {summary(val, prct)}')
print('=' * 40)