from time import sleep
print('\033[1;36m==/\033[m'*8, '\033[1;35mPROGRAMA DE TABUADA\033[m', '\033[1;36m==/\033[m'*8)
i = int(0)
nome = str(input('Digite seu nome:')).capitalize().strip()
num = int(input('Por favor \033[1;33m{}\033[m, digite de qual tabuada você quer o resultado:'.format(nome)))
f = int(input('\033[1;33m{}\033[m agora digite até qual valor você quer o resultado da tabuada do \033[31m{}\033[m:'.format(nome, num)))
print('\033[1;33m{}\033[m por favor aguarde, estou calculando a tabuada do número \033[31m{}\033[m'.format(nome, num))
sleep(3)
print('A tabuada do \033[31m{}\033[m é:'.format(num))
for c in range(i, f+1):
    print('{} x {} = {}'.format(num, c, num*c))
    sleep(1)
print('\033[1;36m==/\033[m'*11, '\033[1;35mFIM\033[m', '\033[1;36m==/\033[m'*11)