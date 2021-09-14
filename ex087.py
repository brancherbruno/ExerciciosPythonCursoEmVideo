#lista limpa para começar
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#comando pra soma dos pares, o maior da segunda linha e a soma dos valores da terceira coluna
somap = mai = somaco = 0
#comando para inserir os valores dentro da lsita, tanto para coluna como para linha
for l in range(0, 3):
    for c in range(0, 3):
        #comando para colocar o valor na linha e coluna a x a
        matriz[l][c] = int(input(f'Digite um valor para [{l} x {c}]: '))
#comando para impressão. Precisa fazer comando for
for l in range(0, 3):
    for c in range(0, 3):
        #comando para centralizar usando ^5
        print(f'[{matriz[l][c]:^5}]', end='')
        #comando para somar os valores pares digitados
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
#comando para somar os valores da última coluna. O comando matriz[l][2] especifica em qual coluna vai ser feita a soma
for l in range(0, 3):
    somaco += matriz[l][2]
#comando para saber o maior valor da linha específica (matriz[1][c])
for c in range(0, 3):
    if c == 0:
        mai += matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'A soma de todos os números pares é: {somap}')
print(f'A soma de todos os números da coluna 3 é: {somaco}')
print(f'O maior valor da linha 2 é: {mai}')
