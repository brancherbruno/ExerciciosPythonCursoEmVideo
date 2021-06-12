from datetime import date
hoje = date.today().year
tma = 0
tme = 0
for pessoas in range(1,8):
    data = int(input('Digite o ano de nascimento da {} pessoa: '.format(pessoas)))
    idd = hoje - data
    if idd >= 18:
        tma += 1
    else:
        tme += 1
print('O número de pessoas com mais de 18 anos é {}'.format(tma))
print('O número de pessoas com menos de 18 anos é {}'.format(tme))
print('ACABOU')
