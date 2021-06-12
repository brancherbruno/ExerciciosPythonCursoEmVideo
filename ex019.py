import random
nome = input('Olá, qual seu nome?')
a = input('{} por favor digite o nome do primeiro aluno:'.format(nome))
b = input('Digite o nome do segundo aluno:')
c = input('Digite o nome do terceiro aluno:')
d = input('Digite o nome do quarto aluno:')
f = [a,b,c,d]
print('O aluno que deverá apagar o quadro será {}'.format(random.choice(f)))
