print('GERADOR DE PA')
print('[==]'*10)
n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
t = n
c = 1
q = 0
m = 10
while m != 0:
    q += m
    while c <= q:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    m = int(input('Quantos termos a mais você quer adicionar?: '))
print('FIM')
print('[=]'*10)
