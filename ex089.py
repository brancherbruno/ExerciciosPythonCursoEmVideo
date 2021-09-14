boletim = []
aluno = []
notas = []
#comando para fazer inserir dados na lista até decisão de parar
while True:
    #código para comando de decisao para continuar ou não
    digi = ' '
    #comando coloca direto na lista o nome
    aluno.append(str(input('Digite o nome do aluno: ')).strip().capitalize())
    #comando para colocar as notas na lista
    for n in range(2):
        notas.append(float(input(f'Digite a {n+1} nota: ')))
    aluno.append(notas[:])
    #comando para saber a média do aluno
    media = (notas[0] + notas[1])/2
    aluno.append(media)
    boletim.append(aluno[:])
    #limpar sempre a lista para não haver sobreposição
    notas.clear()
    aluno.clear()
    #comando para terminar de inserir dados / se a resposta não for S ou N, vai repetir
    while digi not in 'SN':
        digi = str(input('Gostaria de inserir mais dados? [S/N] ')).strip().upper()[0]
    if digi == 'N':
        break
#print formatado para aparecer mais bonito e organizado. os valores são quantas casas e maior e menor a direção
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*24)
#comando para mostrar organizado os valores da lista boletim, neste caso somente a média do aluno
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
#comando para mostrar somente as notas do aluno escolhido
while True:
    cont = int(input('Gostaria de ver as notas de qual aluno? [No.][999 Para parar] '))
    if cont == 999:
        break
    if cont <= len(boletim) -1:
        print(f'As notas de {boletim[cont][0]} são: {boletim[cont][1]}')
print('=*'*22)
