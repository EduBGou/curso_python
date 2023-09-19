def fVote(born):
    from datetime import date
    curret = date.today().year
    age = curret - born
    if age > 18:
        return 'deve votar.'
    elif age < 16:
        return 'não pode votar.'
    else:
        return 'pode votar (opcional).'

born = int(input('Em que ano você nasceu? '))
print(f'Você {fVote(born=born)}')
