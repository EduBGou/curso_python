larger = 0
less = 0

for i in range(1, 5):
    mass = float(input('Digite a {}° massa corporal: '.format(i)))
    if i == 1:
        larger = mass
        less = mass
    else:
        if mass > larger:
            lager = mass
        elif mass < less:
            less = mass
if larger.is_integer():
    larger = int(larger)
if less.is_integer():
    less = int(less)
print('A maior massa corporal é {}Kg, enquanto a menor é {}Kg'.format(larger, less))