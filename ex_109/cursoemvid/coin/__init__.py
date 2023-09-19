def increase(var, amt, show=False):
    return f'{var * ( 1 + (amt / 100)):.2f}' if not show else f'R$ {var * ( 1 + (amt / 100)):.2f}'

def decrease(var, amt, show=False):
    return f'{var * (1 - (amt / 100)):.2f}' if not show else f'R$ {var * (1 - (amt / 100)):.2f}'

def double(value, show=False):
    return f'{value * 2:.2f}' if not show else f'R$ {value * 2:.2f}'
def half(value, show=False):
    return f'{value / 2:.2f}' if not show else f'R$ {value / 2:.2f}'

def summary(value, amt):
    return f'''
Valor Analizado:            R${value:.2f}
Mudança de Porcentagem:     R${value * ( 1 + (amt / 100)):.2f}
Dobro do Valor:             R${value * 2:.2f}
Metade do Valor:            R${value / 2:.2f}'''