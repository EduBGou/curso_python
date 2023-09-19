print('=' * 21)
print('\033[0;32mSISTEMA DE EMPRÉSTIMO\033[m')
print('=' * 21)
print('Calcularemos se é possível realizar um empréstimo conosco, portanto que o valor de cada mensalidade do empréstimo não supere 30% do seu salário mensal. \n(Utilize apenas N° Inteiros).\n')

loanValue = int(input('-> Qual o valor da residência que deseja realizar o empréstimo? R$ '))
salary = int(input('-> Qual o valor do seu salário? R$ '))
Years = int(input('-> Em quantos anos você pretende pagar o empréstimo? '))

pSalary = salary * 0.3
loanValue_Months = loanValue / (Years * 12)

print('-' * 70)
if loanValue_Months <= pSalary:
    print('\033[0;32mMuito bem, seu empréstimo foi aceito. O valor será de R$ {:.2f}/mês;\033[m'.format(loanValue_Months))
else:
    print('\033[0;31mInfelizmente, seu empréstimo não foi aceito pois as parcelas mensais seriam de R$ {:.2f}/mês, \nque excedem 30% do seu salário mensal que é o correspondente à R$ {:.2f};\033[m'.format(loanValue_Months, pSalary))
