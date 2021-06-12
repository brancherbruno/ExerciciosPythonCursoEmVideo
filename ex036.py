from time import sleep
print('\033[1;35m-=-\033[m'*25)
nome = str(input('\033[1;33mOlá, qual seu nome?\033[m')).upper().strip()
casa = float(input('\033[4;31m{}\033[m por favor, qual o valor do imóvel que você pretende adquirir?R$'.format(nome)))
sal = float(input('Qual seu salário atual \033[1;31m{}\033[m?R$'.format(nome)))
ano = int(input('Em quantos anos você pretende quitar o imóvel \033[1;31m{}\033[m?'.format(nome)))
print('Calculando o valor da prestação, por favor aguarde!')
sleep(5)
pre = casa/(ano*12)
if pre <= (sal*0.30):
    print('Parabéns \033[1;36m{}\033[m, você conseguiu o empréstimo da sua tão sonhada moradia! \nSua parcela será de \033[1;31mR${:.2f}\033[m!'.format(nome, pre))
else:
    print('Infelizmente não podemos liberar este empréstimo para você \033[1;32m{}\033[m. \nO valor da parcela é de \033[4;31mR${:.2f}\033[m e excede 30% do seu salário atual.'.format(nome, pre))
print('\033[4;33m-=-\033[m'*25)
