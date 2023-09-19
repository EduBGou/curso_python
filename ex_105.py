def fGrades(grade, sit=False):
    """
    -> Retorna informações sobre as notas
    """
    grade.sort()
    data = {}
    data['n° de registros'] = len(grade)
    data['total'] = sum(grade)
    data['maior'] = max(grade)
    data['menor'] = min(grade)
    data['média'] = data['total'] / data['n° de registros']

    if sit:
        if data['média'] >= 9:
            data['sit'] = 'MUITO BOA'
        elif data['média'] >= 7:
            data['sit'] = 'BOA'
        else:
            data['sit'] = 'RUIM'
    return data

i = 1; show = True
lGrade = []
while True:
    ingrade = int(input(f'{i}º Nota: '))
    i += 1
    lGrade.append(ingrade)
    ask = str(input('Quer continuar? ("N" p/ "Não"): ').upper())
    if ask == 'N':
        showAsk = str(input('Quer Mostrar a Situação? ("N" p/ "Não"): ').upper())
        if showAsk == "N":
            show = False
        break
print(fGrades(lGrade, sit=show))
help(fGrades)