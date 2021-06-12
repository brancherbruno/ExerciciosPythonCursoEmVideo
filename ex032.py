from datetime import date
print('='*45)
nome = str(input('Qual seu nome?')).upper().strip()
ano = int(input('{} por favor digite um ano qualquer ou coloque 0 para analizar o ano atual:'.format(nome)))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('{} o ano {} que você digitou é bissexto.'.format(nome, ano))
else:
    print('{} o ano {} que você digitou não é bissexto.'.format(nome, ano))
print('='*20, 'FIM', '='*20)
