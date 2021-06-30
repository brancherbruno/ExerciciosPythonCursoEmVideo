print('=-'*15)
n = s = c = 0
while True:
    n = int(input('Digite um número [Digite 999 para terminar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números e a soma deles é {s}.')
print('='*10, 'FIM', '='*10)