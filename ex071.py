from time import sleep
print('[]'*10, 'BEM VINDO AO CAIXA ELETRÔNICO 24H', '[]'*10)
v = tno = na = 0
nome = str(input('Por favor digite seu nome: ')).strip().upper()
while True:
    es = ' '
    v = int(input(f'{nome} quanto você gostaria de sacar? R$'))
    if v % 200 and v % 100 and v % 50 and v % 20 and v % 10 and v % 5:
        print('Valor incorreto. Este caixa tem somente notas de: \nR$ 200 \nR$ 100 \nR$ 50 \nR$ 20 \nR$ 10 \nR$ 5')
    else:
        print('Aguarde, calculando...')
        sleep(5)
        total = v
        na = 200
        tno = 0
        while True:
            if total >= na:
                total -= na
                tno += 1
            else:
                if tno > 0:
                    print(f'{nome} você vai sacar {tno} cédulas de R${na}.')
                if na == 200:
                    na = 100
                elif na == 100:
                    na = 50
                elif na == 50:
                    na = 20
                elif na == 20:
                    na = 10
                elif na == 10:
                    na = 5
                tno = 0
                if total == 0:
                    break
    sleep(2)
    while es not in 'SN':
        es = str(input(f'{nome} você gostaria de sacar mais algum valor? [S/N]')).strip().upper()[0]
    if es == 'N':
        break
print(' ')
sleep(3)
print('Obrigado por utilizar o caixa eletrônico 24h')
sleep(2)
print('[]'*10, 'FIM DO PROGRAMA', '[]'*10)
