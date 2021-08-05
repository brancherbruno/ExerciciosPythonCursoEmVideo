from time import sleep
nome = str(input('Digite seu nome: ')).strip().capitalize()
#para colocar os valores em listas distintas, preciso criar as listas vazias
par = []
impar = []
valores = []
while True:
    es = ' '
    valores.append(int(input(f'{nome} digite um valor qualquer: ')))
    while es not in 'SN':
        es = str(input(f'{nome} gostaria de adicionar mais valores? [S/N]: ')).strip().upper()[0]
    if es == 'N':
        break
sleep(2)
valores.sort()
print()
print(f'{nome} os valores digitados foram: {valores}')
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
sleep(2)
print()
impar.sort()
par.sort()
print(f'{nome} os valores ímpares digitados são: {impar}')
sleep(2)
print()
print(f'Já os valores pares digitados são: {par}')
print('=-'*25)
print('FIM DO PROGRAMA')
print('=-'*25)
