print('=-='*25)
nome = str(input('Qual seu nome?')).upper().strip()
n1 = int(input('{} por favor digite um número qualquer:'.format(nome)))
n2 = int(input('Digite outro número qualquer:'))
n3 = int(input('Digite o último número de sua preferência:'))
tma = [n1, n2, n3]
ma = n1
if n2 > ma:
    ma = n2
if n3 > ma:
    ma = n3
tme = [n1, n2, n3]
me = n1
if n2 < me:
    me = n2
if n3 < me:
    me = n3
print('{} o maior número que você digitou é \033[1;31m{}\033[m e o menor é \033[1;36m{}\033[m'.format(nome, ma, me))
print('=-='*25)