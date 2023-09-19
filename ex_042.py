#INPUTS
print('Para ver se é possível formar um \033[0;32mTriângulo\033[m, informe os valores de seus seguimentos.')
side_a = float(input('Digite o valor do segmento 01: '))
side_b = float(input('Digite o valor do segmento 02: '))
side_c = float(input('Digite o valor do segmento 03: '))

#VERIFICAÇÃO SE É POSSÍVEL FORMAR UM TRIÂNGULO
if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_b + side_a:
    print('É possível sim formar um triângulo com as medidas indicadas.')
    #TIPO DE TRIÂNGULO
    if side_a != side_b != side_c != side_a:
        print('Com essas medidas, você forma um triângulo escaleno.')
    elif side_a == side_b == side_c:
        print('com essas medidas, você forma um triângulo equilátero.')
    else:
        print('Com essas medidas você forma um triângulo isóceles.')
else:
    print('Não é possível formar um triângulo com as medidas indicadas.')
