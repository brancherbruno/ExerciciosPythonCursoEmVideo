nome = input('Olá, qual seu nome?')
s = float(input('{} qual seu salário?'.format(nome)))
au = int(input('{} quantos % você gostaria de ganhar de aumento salarial?'.format(nome)))
ns = s+(s*(au/100))
print('{} seu novo salário, acrescido de {}%, é R$ {:.2f}'.format(nome, au, ns))

