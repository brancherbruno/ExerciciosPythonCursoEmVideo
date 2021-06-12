from time import sleep
nome = str(input('Digite seu nome: ')).capitalize().strip()
d = str(input('Olá {}, você gostaria de ver os fogos?'.format(nome))).upper()
if d == 'S' and 'SIM':
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    sleep(0.5)
    print('*'*10, 'FOGOS', '*'*10)
else:
    print('Que pena {}, você vai perder os fogos'.format(nome))
