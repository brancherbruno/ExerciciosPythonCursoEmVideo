import math
nome = input('Olá, qual seu nome?')
co = float(input('{} por favor digite o valor do cateto oposto:'.format(nome)))
ca = float(input('{} agora digite o valor do cateto adjacente:'.format(nome)))
hp = (math.sqrt((math.pow(co,2) + (math.pow(ca,2)))))
#hp = math.hypot(co,ca) - é mais simples de fazer
print('{}, o valor que você digitou, tem como hipotenusa {:.2f}.'.format(nome,hp))