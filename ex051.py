num = int(input('Digite o primeiro termo:'))
r = int(input('Digite o valor da razão:'))
d = num + (10 - 1)*r
for c in range(num, d+r, r):
    print('{}'.format(c), end='-> ')
print('FIM')
