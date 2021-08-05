valor = []
nome = str(input('Digite seu nome: ')).strip().capitalize()
ma = 0
mi = 0
for v in range(0, 5):
    valor.append(int(input(f'{nome} digite um valor qualquer: ')))
    if v == 0:
        ma = mi = valor[v]
    else:
        if valor[v] > ma:
            ma = valor[v]
        if valor[v] < mi:
            mi = valor[v]
print(f'O maior valor digitado foi {ma} ', end='')
for p, v in enumerate(valor):
    if v == ma:
        print(f'na posição {p}.', end='')
print()
print(f'O menor valor digitado foi {mi} ', end='')
for p, v in enumerate(valor):
    if v == mi:
        print(f'na posição {p}.')
print('FIM')
