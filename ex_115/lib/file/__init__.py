def fileExist(fileName):
    try:
        f = open(fileName, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False


def createFile(fileName):
    try:
        f = open(fileName, 'wt+')
        f.close()
    except FileNotFoundError:
        return 'FileNotFoundError'


def readFile(fileName):
    try:
        f = open(fileName, 'rt')
        print(f.read())
        f.close()
        return 'OK'
    except:
        print('ERROR')


def register(fileName, name, age):
    try:
        f = open(fileName, 'at')
        try:
            f.write(f'Nome: {name:20} | Idade: {age}\n')
        except:
            print('Houve um erro ao escrever no arquivo.')
    except:
        print('Houve um erro ao ler o arquivo.')