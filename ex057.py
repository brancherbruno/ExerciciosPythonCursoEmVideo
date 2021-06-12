'''r = 's'               ESSE MEU CÓDIGO DEU ERRADO POIS NAO TEM FIM
while r == 's':
    n = str(input('Digite um nome:')).upper().strip()
    s = str(input('{} é masculino ou feminino? [M/F] '.format(n))).upper().strip()
    if s != 'F' and s != 'M':
        print('Erro na resposta, digite novamente: ')
print('Fim')'''

n = str(input('Digite um nome: ')).strip().capitalize()
s = str(input('Qual o sexo de {}? [M/F]: '.format(n))).upper()
while s not in 'MF':
    s = str(input('Dados incorretos. Por favor digite novamente o sexo de {} [M/F]: '.format(n))).upper()
print('O sexo de {} é {}.'.format(n, s))
