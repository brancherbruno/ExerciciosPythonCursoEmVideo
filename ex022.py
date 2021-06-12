nome = str(input('Olá, qual seu nome completo?')).strip()
print('Por favor aguarde, analisando seu nome...')
print('Seu nome em letras minúsculas fica {}'.format(nome.lower()))
print('Seu nome em letras maiúsculas fica {}'.format(nome.upper()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))











