from random import randint
nome = str(input('Qual seu nome?')).capitalize().strip()
lista = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Escolha:
[0] Pedra
[1] Papel
[2] Tesoura''')
escolha = int(input('Qual sua jogada {}?'.format(nome)))
print('[=]'*9)
print('Você jogou {}'.format(lista[escolha]))
print('O computador escolheu {}'.format(lista[pc]))
print('[=]'*9)
if pc == 0:
    if escolha == 0:
        print('Empate!')
    elif escolha == 1:
        print('Você ganhou!')
    elif escolha == 2:
        print('Você perdeu!')
elif pc == 1:
    if escolha == 0:
        print('Você perdeu!')
    elif escolha == 1:
        print('Empate!')
    elif escolha == 2:
        print('Você ganhou!')
elif pc == 2:
    if escolha == 0:
        print('Você ganhou!')
    elif escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Empate!')

