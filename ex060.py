n = int(input('Por favor digite um número: '))
t = n
f = 1
while t > 0:
    f = f *t
    t -= 1
print('O fatorial de {}! é {}.'.format(n, f))
