n = int(input('N° de Elementos: '))
t1 = 0
t2 = 1
print(f'{t1} => {t2}', end = '')
i = 2
while i < n:
    t3 = t1 + t2
    print(f' => {t3}', end = '')
    t1 = t2
    t2 = t3
    i += 1