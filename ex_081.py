nums = []
while True:
    nums.append(int(input('Digite um número: ')))
    ask = str(input('Deseja continuar? (Se não, digite "N"): ')).upper()
    if ask == "N":
        break
nums.sort(reverse=True)
print(f'\nEsta é a quantidade de números digitados: {len(nums)}.')
print(f'\nEsta é a lista de forma decrescente: {nums}.')
if 5 in nums:
    print(f'\nO valor 5 aparece na lista na posição: {nums.index(5)}.')
else:
    print('\nO valor 5 não se encontra na lista de números.')
