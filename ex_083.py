exp = str(input('\nDigite a expressão: ')).strip()
parA = parF = 0

for i in exp:
    if i == ')':
        parF += 1
        if parA < parF:
            print('\nFechastes um parêntese sem abri-lo.\n')
            break
    if i == '(':
        parA += 1
if parA == parF:
    print('\nSua operação encontra-se sem problemas.\n')
if parA > parF:
    print('\nAbristes um parênteses sem fecha-lo.\n')