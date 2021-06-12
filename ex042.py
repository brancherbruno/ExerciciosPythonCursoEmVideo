from time import sleep
print("\033[32m=\033[m"*35)
nome = str(input('Olá qual seu nome?')).capitalize().strip()
r1 = int(input('\033[34m{}\033[m por favor digite o valor da primeira reta:'.format(nome)))
r2 = int(input('\033[34m{}\033[m digite o valor da segunda reta:'.format(nome)))
r3 = int(input('\033[34m{}\033[m digite o valor da terceira reta:'.format(nome)))
print('\033[31mAguarde, calculando os valores digitados...\033[m')
sleep(4)
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Com os valores de reta que você digitou \033[34m{}\033[m, o triângulo formado é '.format(nome), end='')
    if r1 == r2 == r3:
        print('equilátero!')
    if r1 != r2 == r3 and r1 == r2 != r3 and r1 == r3 != r2:
        print('isósceles!')
    if r1 != r2 != r3:
        print('escaleno!')
else:
    print('Com base nos valores digitados, você não pode formar um triângulo! Tente novamente.')
print('\033[32m=\033[m'*35)
