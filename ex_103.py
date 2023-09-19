def fDataSheet(nam, gl):
    """ 
    -> Não da erro portanto que sejam strings os parâmetros
    :param name = string.
    :param goal = string.
    """
    if nam == '':
        nam = '<unknown>'
    if gl.isnumeric() == False:
        gl = 0
    int(gl)
    return f'{nam} fez {gl} gols.'

# INPUTS
name = str(input('Nome do(a) jogador(a): ').capitalize())
goal = str(input('N° de gols dele(a): '))

# PRINTS
print('=' * 50)
print(fDataSheet(name, goal))
print('=' * 50)