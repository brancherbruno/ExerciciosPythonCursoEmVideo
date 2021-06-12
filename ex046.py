from time import sleep
print('\033[1;33m=**=\033[m'*25)
nome = str(input('Qual seu nome?')).capitalize().strip()
esc = str(input('Preparado para contagem de fogos {}?'.format(nome)))
if esc == 'sim':
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    sleep(1)
    print('\033[1;31m=*=*=*=*=*=FOGOS=*=*=*=*=*=\033[m')
else:
    print('Que pena você vai perder a contagem de fogos {}'.format(nome))
print(' ')
print('=**='*10, 'FIM', '=**='*10)
