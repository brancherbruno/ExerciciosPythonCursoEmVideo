from time import sleep

print('\033[4;36m:=:\033[m' * 25)
nome = str(input('Qual seu nome?')).upper().strip()
n = int(input('{} por favor digite um número:'.format(nome)))
print('1 = Binário \n2 = Octal \n3 = Hexadecimal')
escolha = int(input('{} escolha uma base de conversão:'.format(nome)))
print('\033[1;33mAguarde, em processamento...\033[m')
sleep(3)
if escolha == 1:
    print('O número {} que você escolheu, em código binário é {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {} que você escolheu, em código octal é {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} que você escolheu, em código hexadecimal é {}.'.format(n, hex(n)[2:]))
print('\033[4;36m:=:\033[m' * 25)
