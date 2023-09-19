info = {'name': str(input('Digite um nome: ')).capitalize().strip(), 'med': float(input('Digite a Média de (0 à 10): ')), 'sit': ''}
if info['med'] >= 7:
    info['sit'] = 'Aprovado'
elif 5 <= info['med'] < 7:
    info['sit'] = 'Recuperação'
else:
    info['sit'] = 'Reprovado'

for k, v, in info.items():
    print(f'{k}: {v}.')
