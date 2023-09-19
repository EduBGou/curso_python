import urllib.request
try:
    site = urllib.request.urlopen('https://docs.google.com/document/u/0/')
    print('Deu Certo.')
except:
    print('Não Funcionou Parceiro.')