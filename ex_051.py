firstNum = int(input('Primeiro número: '))
ratio = int(input('Razão: '))
limit = int(input('Limite da PA: '))
last = firstNum + (limit * ratio)
print('(', end = '')
for i in range(firstNum, last, ratio):
    if i == last - ratio:
        print(i, end = ')')
    else:
        print(i, end = ', ')