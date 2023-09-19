words = ('abecitou',
         'arara', 
         'macaco', 
         'pinheiro', 
         'nada',
         'Paralelepípedo')
for p in words:
    print(f'\nA palavra {p.upper()} possui as seguntes vogais: ', end = '')
    for l in p:
        if l.lower() in 'aáàãâeéêiíoõôuú':
            vowel = l
            print(vowel, end = ' ')