from time import sleep
from random import randint
print('='*40)
print('')
print('[=]'*4, 'JOGO DO PAR OU ÍMPAR', '[=]'*4)
print('')
print('='*40)
n = v = r = 0
while True:
    e = ' '
    while e not in 'PI':
        e = str(input('Você escolhe par ou ímpar [P/I]?')).upper().strip()[0]
    n = int(input('Digite um número: '))
    print('Aguarde...')
    sleep(0.7)
    pc = randint(0, 100)
    t = pc + n
    if e == 'P':
        if t % 2 == 0:
            print(f'Parabéns você ganhou! Você jogou {n} e o computador jogou {pc}.')
            v += 1
        else:
            print('Você perdeu! Que pena.')
            break
    elif e == 'I':
        if t % 2 == 1:
            print(f'Parabéns, você ganhou! Você jogou {n} e o computador jogou {pc}.')
            v += 1
        else:
            print('Que pena, você perdeu.')
            break
    sleep(1)
    print('Vamos jogar de novo...')
sleep(0.7)
print(f'Você jogou {n} e o computador jogou {pc} e a soma dos 2 é {t}. Você ganhou {v} vezes.')
sleep(0.7)
print('FIM DE JOGO')
