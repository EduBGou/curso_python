nums = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0 and n != 0:
        nums[0].append(n)  # PAR
    elif n % 2 != 0:
        nums[1].append(n)  # IMPAR
print(f'A lista de forma ordenada de pares é: {sorted(nums[0])}')
print(f'A lista de forma ordenada de ímpares é: {sorted(nums[1])}')
