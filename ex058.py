from random import randint
from time import sleep
no = str(input('Digite seu nome: ')).strip().capitalize()
pc = randint(0, 10)
t = 0
print('O computador irá escolher um número de 0 a 10 agora {}...por favor aguarde...'.format(no))
sleep(3)
nu = True
while nu is not pc:
    nu = int(input('Qual número o computador escolheu {}?: '.format(no)))
    if nu < pc:
        print('Um pouco mais {}...'.format(no))
    elif nu > pc:
        print('Um pouco menos {}...'.format(no))
    t += 1
print('Parabéns {}, você adivinhou o número que o computador escolheu, e levou {} tentativas!'.format(no, t))
