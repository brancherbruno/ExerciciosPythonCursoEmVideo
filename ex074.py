#gerador de números aleatórios
from random import randint
maior = 0
menor = 0
pc1 = randint(0, 100)
pc2 = randint(0, 100)
pc3 = randint(0, 100)
pc4 = randint(0, 100)
pc5 = randint(0, 100)
escolha = pc1, pc2, pc3, pc4, pc5
print('Os valores escolhidos são: ')
for n in escolha:
    print(f'{n}', end='  ')
print(' ')
print(f'O maior valor escolhido foi {max(escolha)}')
print(f'O menor valor escolhido foi {min(escolha)}')

