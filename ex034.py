print('=-='*25)
nome = str(input('Qual seu nome?')).upper().strip()
sa = float(input('{} qual seu salário atual?'.format(nome)))
if sa > 1250:
    v1 = sa + (sa*0.10)
    print('{} seu salário novo será de R${:.2f}'.format(nome, v1))
else:
    v2 = sa + (sa*0.15)
    print('{} seu salário será de R${:.2f}'.format(nome, v2))
print('=-='*25)