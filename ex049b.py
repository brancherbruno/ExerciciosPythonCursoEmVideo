n = int(input('Digite um número: '))
print('A tabuada do {} é:'.format(n))
for c in range(1, 11):
    n1 = c*n
    print('{} x {} = {}'.format(n, c, n1))