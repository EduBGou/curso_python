# CRIAR UMA LISTA E DPS CRIAR 2 OUTRAS, UMA PARA PAR E OUTRA PARA IMPAR
nums = []; imp = []; par = []
while True:
    nums.append(int(input('Digite um número: ')))
    if nums[-1] % 2 == 0:
        par.append(nums[-1])
    else:
        imp.append(nums[-1])
    ask = str(input('Quer progesseguir? ("N" para não): ')).strip().upper()
    if ask == 'N':
        break
print(f'A lista de forma ordenada é: {sorted(nums)}')
print(f'A lista de forma ordenada de pares é: {sorted(par)}')
print(f'A lista de forma ordenada de ímpares é: {sorted(imp)}')