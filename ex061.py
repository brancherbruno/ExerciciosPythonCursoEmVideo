n = int(input('Digite um valor: '))
r = int(input('Digite a razão: '))
t = n
c = 1
while c <= 10:
    print('{} -> '.format(t), end='')
    t += r
    c += 1
print('FIM')
