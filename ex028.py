import random
from time import sleep
print('='*20)
nome = str(input('Por favor qual seu nome?')).upper().strip()
lista = [0,1,2,3,4,5]
pc = random.choice(lista)
n = int(input('{} o computador irá escolher um número de 0 a 5. Qual número o computador escolheu?'.format(nome)))
print('Processando...')
sleep(3)
if n == pc:
    print('Parabéns {}, você adivinhou o número!'.format(nome))
else:
    print('{} infelizmente você não acertou o número escolhido que era o número {}'.format(nome, pc))
print('='*12, 'FIM', '='*12)

#mais simples é usar randint (0, 5)