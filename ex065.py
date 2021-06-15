from time import sleep
print('[=]'*20)
print('')
c = s = m = ma = me = 0
d = ''
while d in 'S':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    d = str(input('Gostaria de adicionar mais números? [S/N]')).upper().strip()[0]
m = s/c
print('Calculando...')
sleep(1.5)
print('A média dos valores é {:.0f} e você digitou {} números.'.format(m, c))
print('Calculando...')
sleep(1.5)
print('O valor maior é {} e o valor menor é {}'.format(ma, me))
sleep(2)
print('')
print('[=]'*8, 'Terminou', '[=]'*8)
