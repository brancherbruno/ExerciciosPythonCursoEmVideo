n = int(input('Digite um valor'))
r = int(input('Digite a razão:'))
pa = n + (10 - 1) * r
for c in range(n, pa+r, r):
    print(c, end=' ')
