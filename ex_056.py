sumAge = 0
oldermanAge = 0
oldermanName = ''
underageWoman = 0
i = 0
while i < 4:
    name = str(input('Digite o {}° nome: '.format(i + 1))).strip()
    age = int(input('Digite a {}° idade: '.format(i + 1)))
    sex = str(input('Digite o {}° sexo (M/F): '.format(i + 1))).strip().lower()
    print('')
    sumAge += age

    if i == 0 and sex == 'm':
        oldermanAge = age
        oldermanName = name

    elif sex == 'm':
        if age > oldermanAge:
            oldermanAge = age
            oldermanName = name
        elif age == oldermanAge:
            oldermanName += 'e' + name
    
    if sex == 'm' and age < 20:
        underageWoman += 1
    i += 1

averageAge = age / 4
print('A média da idade do grupo é {} anos'.format(averageAge))
print('O(s) homem(ns) mais velho(s) é(são) {}, que tem(têm) {} anos'.format(oldermanName, oldermanAge))
print('Há {} mulheres com menos de 20 anos.'.format(underageWoman))