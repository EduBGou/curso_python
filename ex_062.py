firstNum = int(input('Primeiro número: '))
ratio = int(input('Razão: '))
limit = int(input('Limite da PA: '))
result = 0
i = limit
print('(', end = '')
while i > 0:
    if i != limit:
        result += ratio
    if i == 1:
        print(firstNum + result, end = ')')
    else:
        print(firstNum + result, end = ', ')
    i -= 1