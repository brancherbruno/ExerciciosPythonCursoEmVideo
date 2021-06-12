from random import choice
from time import sleep
print('\033[34m[:]=\033[m'*35)
nome = str(input('Por favor, digite seu nome:')).capitalize().strip()
print('Seja bem vindo(a) \033[1;32m{}\033[m! Vamos jogar Jokenpô!'.format(nome))
print('\033[31m1 = Pedra\033[m \n\033[33m2 = Papel\033[m \n\033[36m3 = Tesoura\033[m')
pedra = 1
papel = 2
tesoura = 3
lista = [1, 2, 3]
pc = choice(lista)
j = int(input('Faça sua escolha \033[1;32m{}\033[m:'.format(nome)))
print('\033[31mJo...ken....pô!\033[m')
sleep(1)
if j == 1 and pc == 2:
    print('Você perdeu \033[1;32m{}\033[m! Você escolheu pedra e eu escolhi papel. Eu ganhei :)'.format(nome))
elif j == 1 and pc == 3:
    print('Parabéns \033[1;32m{}\033[m! Você escolheu pedra e eu tesoura. Eu perdi :('.format(nome))
elif j == 2 and pc == 1:
    print('Parabéns \033[1;32m{}\033[m! Você escolheu papel e eu pedra. Eu perdi :('.format(nome))
elif j == 2 and pc == 3:
    print('Você perdeu \033[1;32m{}\033[m! Você escolheu papel e eu tesoura. Eu ganhei :)'.format(nome))
elif j == 3 and pc == 1:
    print('Você perdeu \033[1;32m{}\033[m! Você escolheu tesoura e eu pedra. Eu ganhei :)'.format(nome))
elif j == 3 and pc == 2:
    print('Parabéns \033[1;32m{}\033[m! Você escolheu tesoura e eu papel. Eu perdi :('.format(nome))
else:
    print('Empatamos! Ninguém ganhou! Você escolheu {} e eu também!'.format(j))
print('\n')
print('\033[34m[:]=\033[m'*10, 'FIM DE JOGO', '\033[34m[:]=\033[m'*10)
