#INPUTS
value = float(input('Qual o valor da compra? R$ '))
payMethod = int(input('Qual método de pagamento você deseja realizar? \n[1] Dinheiro/Cheque; \n[2] Cartão; \nDigite aqui: '))

if payMethod == 2:
    instll = int(input('Em quantas prestações você deseja pagar? (Digite [1] se for à vista): '))
    
#CASO DIGITE UM N° INVÁLIDO
    if instll <= 0:
        print('Esse N° é inválido.')
elif payMethod > 2:
    print('Esse N° é inválido.')
    
#DINHEIRO OU CHEQUE
if payMethod == 1:
    value = value * 0.9
    print('O novo valor da compra será de R$ {:.2f}, devido à um desconto de 10%.'.format(value))

#CARTÃO
if payMethod == 2:

    #1X
    if instll == 1:
        value = value * 0.95
        instll_value = value / instll
        print('O novo valor da compra será de R$ {:.2f}, devido ao desconto de 5%.'.format(value))
    #2X
    elif instll == 2:
        instll_value = value / instll
        print('O valor da compra será de R$ {:.2f}, sem juros, em {} parcelas de R$ {:.2f}/mês.'.format(value, instll, instll_value))
    #3X
    elif instll >= 3:
        value = value * 1.2
        instll_value = value / instll
        print('O novo valor da compra será de R$ {:.2f}, devido ao juros de 20%, em {} parcelas de R$ {:.2f}/mês.'.format(value, instll, instll_value))