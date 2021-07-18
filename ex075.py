nt = 0
np = 0
val = (int(input('Digite um primeiro valor: ')),
           int(input('Digite um segundo valor: ')),
           int(input('Digite um terceiro valor: ')),
           int(input('Digite um quarto valor: ')))
print(f'Você digitou os números: {val}')
#contando quantas vezes o número 9 foi digitado.
#pode ser feito mais simplificadamente como: print(f'O valor 9 apareceu {val.count(9) vezes}'
for c in val:
    if c == 9:
        nt += 1
    if c % 2 == 0:
        np += 1
print(f'Foram digitados {nt} vezes o número 9.')
print(f'Você digitou {np} números pares.')
#para saber o lugar aonde qualquer valor se encontra:
if 3 in val:
    print(f'O valor 3 apareceu na posição número {val.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print('FIM')
