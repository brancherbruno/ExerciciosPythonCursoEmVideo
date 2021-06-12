nome = input('Olá, qual seu nome?')
b = float(input('{} por favor digite a largura da parede:'.format(nome)))
h = float(input('{} agora por favor digite a altura da parede:'.format(nome)))
a = b*h
t = a/2
print('{}, a parede que você pretende pintar tem {} m2 e você precisará de {:.0f} litros de tinta para pintar toda a parede.'.format(nome, a, t))