info = [[[]], [[]], [[]], [[]]]
med = 0

while True:
    info[0].append(str(input('\nDigite o Nome do(a) Aluno(a): ')).capitalize())
    info[1].append(float(input('Digite a Primeira Nota do(a) Aluno(a): ')))
    info[2].append(float(input('Digite a Segunda Nota do(a) Aluno(a): ')))
    ask = str(input('Quer continuar? ("N" para não): ')).strip().upper()
    if ask == 'N':
        break

for i in range(1, len(info[0])):
    med = (info[1][i] + info[2][i]) / 2
    if i == 1:
        print(f'\n{"N° ":=<5}', end=' ')
        print(f'{"Nome ":=<15}', end=' ')
        print(f'{"Média"}')
    print(f'{i:<5} ', end='')               # N°
    print(f'{info[0][i]:<15} ', end='')     # NOME
    print(f'{med:.1f}')                     # MEDÍA
    ask = i + 1
print('')
while True:
    while ask < 0 or ask > i:
        ask = int(input('Digite o N° do(a) aluno(a) para ver suas informações ("0" para sair do programa): '))
    if ask == 0:
        break
    print(f'\nAluno(a) de N° {ask}:')
    print(f'Nome: {info[0][ask]}')
    print(f'Primeira Nota: {info[1][ask]}')
    print(f'Segunda Nota: {info[2][ask]}')
    med = (info[1][ask] + info[2][ask]) / 2
    print(f'Média: {med:.1f}')
    ask = i + 1

print('\nPrograma Executado com Sucesso!')
