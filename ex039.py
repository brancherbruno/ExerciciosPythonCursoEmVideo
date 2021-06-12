from time import sleep
from datetime import date
print('\033[1;35m<==>\033[m' * 35)
nome = str(input('Olá, qual seu nome?')).capitalize().strip()
ano = int(input('\033[1;31m{}\033[m por favor digite o ano de seu nascimento (ex: 9999):'.format(nome)))
hoje = date.today().year
idd = hoje-ano
print('\033[1;31m{}\033[m \033[1;33maguarde enquanto processo o valor...\033[m'.format(nome))
sleep(3)
if idd == 18:
    print('\033[1;31m{}\033[m está na hora de se alistar!'.format(nome))
elif idd < 18:
    t1 = 18-idd
    print('Faltam ainda \033[1;33m{}\033[m anos para seu alistamento \033[1;31m{}\033[m!'.format(t1, nome))
elif idd > 18:
    t2 = idd-18
    print('Você já passou \033[1;33m{}\033[m anos do prazo de alistamento \033[1;31m{}\033[m!'.format(t2, nome))

print('Obrigado por utilizar o programa \033[1;31m{}\033[m, tenha um bom dia!'.format(nome))
print('\033[1;35m<==>\033[m' * 35)
