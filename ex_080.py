nums = []
for i in range(0, 5):
    nums.append(int(input('\nDigite um número: ')))
    num = nums[:]
    
    for c in range(0, len(nums)):
        if num[i] < nums[c]:
            nums.insert(c, num[i])
            nums.pop()
            break

    if nums.index(num[i]) == len(nums) - 1:
        print(f'{num[i]} foi adicionado ao final da lista.')
    else:
        print(f'{num[i]} está na posição {nums.index(num[i])} da lista.')
print(f'\nEssa é a lista de forma ordenada: {nums}.')