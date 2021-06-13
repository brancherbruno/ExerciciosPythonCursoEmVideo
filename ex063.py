print('='*59)
s = int(input('Quantos elementos da sequência de Fibonacci você quer ver?: '))
n1 = 0
n2 = 1
c = 3
print('{} -> {} '.format(n1, n2), end='')
while c <= s:
    n3 = n1 + n2
    print('-> {}'.format(n3), end=' ')
    n1 = n2
    n2 = n3
    c += 1
print('-> FIM')
print('=='*29)
print('FIM')
