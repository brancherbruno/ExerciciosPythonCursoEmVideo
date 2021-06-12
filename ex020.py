import random

nome = input('Olá, digite seu nome:')
a = input('Por favor digite o nome do primeiro aluno:')
b = input('Digite o nome do segundo aluno:')
c = input('Digite o nome do terceiro aluno:')
d = input('Digite o nome do quarto aluno:')
alunos = [a,b,c,d]
random.shuffle(alunos)
print('A ordem de apresentação dos trabalhos será: {}'.format(alunos))




