info = {}
info['name'] = str(input('Nome do jogador: ').strip().capitalize())
info['amtMatches'] = int(input('N° de partidas: '))
info['goalMatche'] = list()
info['total'] = 0
for i in range(0, info['amtMatches']):
    info['goalMatche'].append(int(input(f'Qaantos gols foram marcados na partida {i + 1}? ')))
    info['total'] += info['goalMatche'][-1]

print(f'\nO jogador {info["name"]} obteve um total de {info["total"]} gols.')

for i in range(0, info['amtMatches']):
    print(f'Na partida {i + 1}, {info["name"]} marcou {info["goalMatche"][i]} gol(s).')
