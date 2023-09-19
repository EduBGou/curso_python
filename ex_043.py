mass = float(input('Qual a sua massa corporal em kilogramas?: '))
height = float(input('Qual é a sua altura em metros? '))

imc = mass / (height ** 2)
print('Seu IMC é de: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso recomendado.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está sobrepeso.')
elif 30 <= imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')