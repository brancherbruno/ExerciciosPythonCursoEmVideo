num = int(input('Digite um número:'))
t = 0
for c in range(1, num + 1):
    if num % c == 0 and num % 1 == 0:
        t += 1
if t == 2:
    print('É primo')
else:
    print('Não é primo')
print('FIM')
