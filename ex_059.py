result = 0
start = True

while start:
    operation = int(input('Digite a operação que você deseja realizar. \n[0] Maior/Menor \n[1] Soma; \n[2] Subtração; \n[3] Divisão; \n[4] Multiplicação; \n[5] Sair do Programa; \nDigite aqui a sua escolha: '))
    if operation == 5:
        start = False
    else:
        valueA = float(input('Digite o primeiro termo da operação: '))
        valueB = float(input('Digite o segundo termo da operação: '))
        if operation == 0:
            if valueA > valueB:
                larger = valueA
                less = valueB
                isSame = False
            elif valueB > valueA:
                larger = valueB
                less = valueA
                isSame = False
            else:
                isSame = True
        elif operation == 1:
            result = valueA + valueB
        elif operation == 2:
            result = valueA - valueB
        elif operation == 3:
            result = valueA / valueB
        elif operation == 4:
            result = valueA *  valueB
        elif 0 <= operation >= 6:
            print('Digite uma resposta válida.')
    if operation == 0:
        if isSame:
            print('Ambos os números são {}.'.format(valueA))
        else:
            print('O maior número é o {}, enquanto o menor é {}'.format(larger, less))
    else:
        print('O resultado da operação {} entre {} e {} é = {}.\n'.format(operation, valueA, valueB, result))