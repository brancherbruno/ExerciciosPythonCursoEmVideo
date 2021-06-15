print('=='*25)
n = c = s = 0
n = int(input('Digite um número: [Para parar digite 999] '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número: [Para parar digite 999] '))
print('Você digitou {} termos e a soma dos valores é {}.'.format(c, s))
print('=='*15, 'FIM', '=='*15)
