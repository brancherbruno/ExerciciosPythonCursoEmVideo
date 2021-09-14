from random import randint
matriz = []
jogos = []
tot = 1
d = int(input('Quantos jogos você quer fazer? '))
while tot <= d:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in matriz:
            matriz.append(n)
            c += 1
        if c >= 6:
            break
    matriz.sort()
    jogos.append(matriz[:])
    matriz.clear()
    tot += 1
for j, i in enumerate(jogos):
    print(f'Jogo {j+1} é: {i}')
