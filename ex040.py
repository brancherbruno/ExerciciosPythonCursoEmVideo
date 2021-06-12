from time import sleep
print('\033[31m##==\033[m'*35)
nome = str(input('Por favor qual seu nome?')).upper().strip()
n1 = float(input('\033[35m{}\033[m por favor digite a sua primeira nota:'.format(nome)))
n2 = float(input('Digite sua segunda nota \033[35m{}\033[m:'.format(nome)))
n3 = float(input('Digite sua terceira nota \033[35m{}\033[m:'.format(nome)))
n4 = float(input('\033[35m{}\033[m agora digite sua última nota:'.format(nome)))
m = (n1+n2+n3+n4)/4
print('\033[36mAguarde estamos calculando sua média!\033[m')
sleep(4)
if m >= 7.0:
    print('Parabéns \033[35m{}\033[m, sua média foi de \033[32m{:.2f}\033[m e você passou de ano!'.format(nome, m))
elif 5.0 <= m <= 6.9:
    print('Infelizmente sua nota foi \033[33m{:.2f}\033[m e você ficou de recuperação \033[35m{}\033[m!'.format(m, nome))
elif m < 5.0:
    print('Você não estudou suficiente, sua média foi de \033[31m{:.2f}\033[m e foi reprovado \033[35m{}\033[m!'.format(m, nome))
print('\033[31m##==\033[m'*35)
