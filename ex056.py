sidd = 0
idma = 0
nv = ''
idme = 0
for p in range(1, 5):
    print('---------- {} PESSOA ----------'.format(p))
    nome = str(input('Digite o nome: ')).capitalize()
    idd = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F}')).strip().upper()
    sidd += idd
    if p == 1 and sexo == 'M':
        idma = idd
        nv = nome
    if sexo == 'M' and idd > idma:
        idma = idd
        nv = nome
    if sexo == 'F' and idd < 20:
        idme += +1
midd = sidd / 4
print('A média de idade do grupo é {} anos.'.format(midd))
print('O homem mais velho tem {} e se chama {}.'.format(idma, nv))
print('{} mulher(es) tem menos de 20 anos.'.format(idme))
print('FIM')
