from time import sleep
from datetime import date
print('\033[32m-_-\033[m'*35)
nome = str(input('Bem vindo ao programa da CNN (Confederação Nacional de Natação. Digite seu nome:')).capitalize().strip()
nasc = int(input('\033[31m{}\033[m por favor digite o ano de seu nascimento (ex: 9999):'.format(nome)))
hoje = date.today().year
idd = hoje - nasc
print('\033[36mAguarde enquanto calculamos qual categoria você vai estar...\033[m')
sleep(4)
if idd <= 9:
    print('Sua categoria é \033[36mMIRIM\033[m.')
elif idd <= 14:
    print('Sua categoria é \033[36mINFANTIL\033[m.')
elif idd <= 19:
    print('Sua categoria é \033[36mJUNIOR\033[m.')
elif idd <= 20:
    print('Sua categoria é \033[36mSÊNIOR\033[m.')
elif idd > 20:
    print('Sua categoria é \033[36mMASTER\033[m.')
print('Obrigado por utilizar o programa da CNN \033[31m{}\033[m, tenha um ótimo dia!'.format(nome))
print('\033[32m-_-\033[m'*35)
