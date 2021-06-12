from time import sleep
print('\033[1;36m[==]\033[m'*35)
nome = str(input('Olá qual seu nome?')).capitalize().strip()
valor = float(input('\033[31m{}\033[m por favor digite o valor do produto que você deseja comprar R$'.format(nome)))
print('[1] = Dinheiro/Cheque \n[2] = À vista no Cartão \n[3] = Crédito em 2x \n[4] = Crédito em 3x ou mais')
pgto = int(input('\033[31m{}\033[m qual o método de pagamento?'.format(nome)))
print('\033[1;33mAguarde, estamos processando o valor da compra...\033[m')
sleep(5)
if pgto == 1:
    print('\033[31m{}\033[m o valor da compra fica R${:.2f}.'.format(nome, valor-(valor*(10/100))))
elif pgto == 2:
    print('\033[31m{}\033[m o valor da compra fica R${:.2f}'.format(nome, valor-(valor*(5/100))))
elif pgto == 3:
    print('\033[31m{}\033[m o valor da compra fica dividido em 2 parcelas de R${} e no total fica R${:.2f}'.format(nome, valor/2, valor))
elif pgto == 4:
    total = valor+(valor*(20/100))
    tparc = int(input('Em quantas parcelas você deseja fazer?'))
    print('\033[31m{}\033[m o valor da compra fica dividido em {} parcelas e cada uma no valor de R${:.2f} totalizando R${:.2f}'.format(nome, tparc, total/tparc, valor+(valor*(20/100))))
print('Obrigado(a) por comprar com a gente {}! Agradecemos a preferência. Volte sempre!'.format(nome))
print('\033[1;36m[==]\033[m'*35)