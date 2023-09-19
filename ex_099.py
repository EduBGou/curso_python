choice = int(input('\nEscolha seu método para resolver este exercício (1 ou 2): '))
if choice == 1:
    def bigger(n):
        n.sort()
        print(f'\nAo todo foram inseridos {len(n)} valores, sendo o maior: {n[-1]}')
    num = []
    while True:
        num.append(int(input('Digite um número: ')))
        if len(num) >= 2:
            ask = str(input('Deseja Inserir mais um número? (N para Não): ')).upper()
            if ask == 'N':
                break
    bigger(num)
elif choice == 2:
    def bigger(*n):
        value = big = 0
        for i in n:
            if i == 0:
                big = value
            elif value > big:
                big = value
        print(f'\nAo todo foram inseridos {len(n)} valores, sendo o maior: {n[-1]}\n')
    bigger(2, 6, 18, 44)
