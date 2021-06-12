from time import sleep
print('\033[1;34m<=>\033[m'*35)
nome = str(input('Por favor digite seu nome:')).capitalize().strip()
n1 = int(input('\033[1;31m{}\033[m digite um valor qualquer:'.format(nome)))
n2 = int(input('\033[1;31m{}\033[m por favor digite um segundo valor qualquer:'.format(nome)))
print('\033[1;31m{}\033[m \033[1;33mpor favor aguarde, estou validando os valores...\033[m'.format(nome))
sleep(5)
if n1 == n2:
    print('Não existe valor maior, os valores \033[1;36m{}\033[m e \033[1;36m{}\033[m são iguais.'.format(n1, n2))
elif n1 > n2:
    print('O valor \033[1;33m{}\033[m digitado primeiro é maior!'.format(n1))
elif n2 > n1:
    print('O valor \033[1;35m{}\033[m digitado por segundo é maior!'.format(n2))
print('Obrigado por utilizar meu programa \033[1;31m{}\033[m, tenha um bom dia!'.format(nome))

print('\033[1;34m<=>\033[m'*35)
