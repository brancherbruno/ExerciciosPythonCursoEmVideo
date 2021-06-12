#import math
#para rodar o strip no final do input, o valor deve ser de tipo str e nao int.
#num = str(input('Olá, por favor digite um número inteiro de até 4 dígitos:')).strip()
print('='*28)
num = int(input('Digite um número'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))

print('A unidade do número {} é {}'.format(num, u))
print('A dezena do número  {} é {}'.format(num, d))
print('A dezena do número  {} é {}'.format(num, c))
print('A centena do número {} é {}'.format(num, m))

#print('A unidade do número {} é {} \n A dezena do número {} é {} \n A centena do número {} é {} \n O milhar do número {} é {}'.format(num, math.fabs(num)))

#print('A unidade do número {} é {}'.format(num, num[3]))
#print('A dezena  do número {} é {}'.format(num, num[2]))
#print('A centena do número {} é {}'.format(num, num[1]))
#print('O milhar  do número {} é {}'.format(num, num[0]))
print('='*28)