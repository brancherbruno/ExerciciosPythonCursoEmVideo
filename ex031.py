print('='*45)
nome = str(input('Qual seu nome?')).upper().strip()
d = float(input('{} quantos km vai ter a viagem que você deseja fazer?'.format(nome)))
if d <= 200:
    t = d*0.50
    print('{} a sua viagem vai custar R${:.2f}'.format(nome,t))
else:
    t2 = d*0.45
    print('{} a sua viagem custará R${:.2f}'.format(nome,t2))
print('='*15, 'FIM', '='*15)
