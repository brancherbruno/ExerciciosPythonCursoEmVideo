from datetime import date
hoje = date.today().year
ma = 0
me = 0
for idades in range(1, 8):
    ano = int(input('Digite um ano de nascimento da {} pessoa (ex: 2021):'.format(idades)))
    idd = hoje - ano
    if idd >= 18:
        ma += 1
    else:
        me += 1
print('{} pessoas tem mais de 18 anos por isso são maiores de idade..'.format(ma))
print('{} pessoas são menores de 18 anos e por isso são menores de idade.'.format(me))
