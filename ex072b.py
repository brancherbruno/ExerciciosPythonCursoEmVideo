nome = str(input('Por favor digite seu nome: ')).strip().upper()
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    c = ' '
    num = int(input(f'{nome} digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        print(f'{nome} você digitou {cont[num]}.')
    print(f'{nome} tente novamente.', end='')
    while c not in 'SN':
        c = str(input(f'{nome} deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
print('Fim do Programa')
