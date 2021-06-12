nome = input('Olá, qual seu nome?')
di = float(input('Olá {} tudo bem? Você poderia digitar quantos reais você tem em sua carteira agora?'.format(nome)))
do = di/3.27
print('{}, no momento você pode comprar aproximadamente $ {:.2f} dólares'.format(nome,do))
