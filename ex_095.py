info = {'goalMatche': []}
guys = []
goal = ii = 0

# INPUTS
while True:
    info['name'] = str(input('\nNome do(a) jogador(a): ').strip().capitalize())
    info['amtMatche'] = int(input('N° de partidas: '))
    info['goalMatche'].append(list())

    for i in range(0, info['amtMatche']):
        goal = int(input(f'Quantos gols foram marcados na {i + 1}° partida? '))
        info['goalMatche'][ii].append(goal)

    info['totalGoal'] = sum(info['goalMatche'][ii])
    guys.append(info.copy())
    ask = str(input('Quer continuar (N para "Não"): ')).upper()
    ii += 1
    if ask == 'N':
        break

# PRINTS
print('=' * 70)
print(f'{"CÓDIGO":<6} | {"NOME":<15} | {"GOLS":<30} | {"TOTAL":<5}')
ii = 0
for i, v in enumerate(guys):
    print(f'{i + 1:<6} | {v["name"]:<15} | {str(v["goalMatche"][ii]):<30} | {str(v["totalGoal"]):<5}')
    ii += 1
print('=' * 70)

while True:
    while True:
        askData = int(input('Digite o códido de um(a) jogador(a) para ver suas estatíticas ("0" para Finalizar): ')) - 1
        if askData == -1:
            break
        if 0 <= askData < len(guys):
            break
    if askData == -1:
        print('Programa finalizado com sucesso!')
        break
    print(f'\nInformações do(a) jogador(a): {guys[askData]["name"]}.')
    print(f'Código: {askData + 1}')
    print(f'Total de gols: {guys[askData]["total"]}')
    print('Gol(s) em cada partida: ')
    for i in range(0, guys[askData]["amtMatche"]):
        print(f'    Partida {i + 1}, marcou: {info["goalMatche"][askData][i]} gols.')
    print()