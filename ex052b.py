n = int(input('Digite um número qualquer:'))
t = 0
for c in range(1, n+1):
    if n % c == 0 and n % 1 == 0:
        t += 1
if t == 2:
    print('O número {} escolhido é primo.'.format(n))
else:
    print('O número {} escolhido não é primo.'.format(n))
