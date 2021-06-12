nome = input('Olá, por favor digite seu nome:')
n1 = float(input('{} por favor digite a sua primeira nota:'.format(nome)))
n2 = float(input('{} agora digite sua segunda nota:'.format(nome)))
n3 = float(input('{} agora digite sua terceira nota:'.format(nome)))
n4 = float(input('{} por fim digite a nota da sua última prova:'.format(nome)))
m = (n1 + n2 + n3 + n4) / 4
print('{} pelas notas que você tirou, sua média ficou em {:.2f}'.format(nome,m))
