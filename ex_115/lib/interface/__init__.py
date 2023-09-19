def fLine(size=50):
    print('=' * size)

def fHeader(msg='', size=50):
    fLine(size)
    print(f'{msg:^50}')
    fLine(size)

def fMenu(*msg):
    fHeader('\033[1;36mMENU PRINCIPAL\033[m')
    for i in range(0, len(msg)):
        print(f'{i + 1} - {msg[i]}')
    fLine()

