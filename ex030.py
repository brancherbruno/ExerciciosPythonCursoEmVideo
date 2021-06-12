import math
print('==-'*20)
nome = str(input('Por favor, qual seu nome?')).strip()
n = float(input('{} digite um número qualquer:'.format(nome)))
r = n % 2
if r == 0:
    print('{} o número que você digitou é par.'.format(nome))
else:
    print('{} o número que você digitou é ímpar.'.format(nome))

print('==-'*20)
