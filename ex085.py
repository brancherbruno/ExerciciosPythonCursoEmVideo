#lista em branco iterada
de = [[], []]
#código para fazer a leitura de 7 valores
for p in range(0, 7):
    #vou jogar o valor v fora da lista pois depois de saber se é impar ou par que eu vou jogar dentro da lista.
    v = int(input(f'Digite o {p+1} valor: '))
    #codigo para saber se é impar ou par
    if v % 2 == 0:
        #colocar de[0] significa que vou colocar o valor v na posicao zero da lista, se for par
        de[0].append(v)
        #o sort é pra colocar em ordem, já a lista
        de[0].sort()
    else:
        de[1].append(v)
        de[1].sort()
print(f'Os valores pares digitados são: {de[0]}')
print(f'Os valores ímpares digitados são: {de[1]}')
print(de)
