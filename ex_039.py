from datetime import date

born = int(input('Em que ano você nasceu? '))
today = int(date.today().year)
age = today - born
difAge = age - 18
if difAge < 0:
    difAge = difAge * -1

if age < 18:
    print('Você ainda não pode se alistar no exército, pois possui apenas {} anos, logo falta(m) {} ano(s).'.format(age, difAge))
elif age == 18:
    print('Você já tem idade p/ se alistar no exército, pois têm exatos {} anos.'.format(age))
else:
    print('Você não pode mais se alistar no exército, pois têm {} anos, ou seja, passou {} ano(s) do que deveria'.format(age, difAge))