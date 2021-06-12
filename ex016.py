import math
nome = input('Olá, digite seu nome:')
n = float(input('{} por favor digite um número qualquer:'.format(nome)))
print('O número {} que você digitou {}, tem a parte inteira {}'.format(n, nome, (math.trunc(n))))
