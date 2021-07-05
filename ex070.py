c1 = pre = pme = c2 = tot = 0
mp = ' '
print('='*10, 'COMPRA DE PRODUTOS', '='*10)
n = str(input('Por favor digite seu nome: ')).strip().upper()
while True:
    de = ' '
    pro = str(input(f'Por favor {n} digite o nome do produto: ')).strip().upper()
    pre = float(input(f'{n} agora digite o preço do produto {pro}: R$'))
    c2 += 1
    tot += pre
    if pre > 1000:
        c1 += 1
    if c2 == 1 or pre < pme:
        pme = pre
        mp = pro
    while de not in 'SN':
        de = str(input(f'{n} você gostaria de continuar a incluir produtos e preços? [S/N]')).strip().upper()[0]
    if de == 'N':
        break
print(' ')
print('[=]'*10, 'FINALIZANDO', '[=]'*10)
print(f'{n} o total gasto na sua compra foi R$ {tot:.2f} \n{c1} produtos custam mais de R$ 1.000,00 \n{mp} é o produto mais barato.')
print(f'{n} obrigado por usar o programa de cadastro de produtos!')
