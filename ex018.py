import math

nome = input('Olá, digite seu nome')
a = float(input('{} digite o valor de um ângulo qualquer:'.format(nome)))
#sempre que for usar ângulos converter para radianos pois o python entende como número real e nao radianos para calcular
b = math.radians(a)
print('{} o valor do ângulo digitado tem como \n seno {:.2f}\n coseno {:.2f} \n tangente {:.2f}'.format(nome, math.sin(b), math.cos(b), math.tan(b)))
