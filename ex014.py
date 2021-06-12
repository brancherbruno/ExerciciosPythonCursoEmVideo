nome = input('Olá, qual seu nome?')
c = float(input('{} por favor digite a temperatura atual em graus celcius:'.format(nome)))
f = (c*1.8)+32
k = c+273.15
print('{}, a temperatura de {}C em fahrenheit é {} e em kelvin é {:.2f}.'.format(nome,c,f,k))