nome = str(input('Digite seu nome: ')).strip().capitalize()
lista = []
while True:
    #valor do es em branco para poder funcionar o while de pergunta para continuar digitando valores
    es = ' '
    lista.append(int(input(f'{nome} digite um valor: ')))
    #comando para saber se o usuário quer continuar usar o programa
    while es not in 'SN':
        es = str(input(f'{nome} deseja continuar digitando valores? [S/N]:')).strip().upper()[0]
    if es == 'N':
        break
print()
if 5 not in lista:
    print(f'O número 5 não foi digitado {nome}.')
else:
    print(f'O número 5 foi inserido e está na lista.')
print()
#no len(lista que você produziu) conta quantos valores estão dentro da lista. (se for palavras ele vai contar quantas
#palavras tem dentro da lista...
print(f'{nome} você digitou {len(lista)} números, são eles: {lista}.')
print()
#colocando em ordem decrescente a lista - a partir daqui a lista será sempre impressa em ordem decrescente.
lista.sort(reverse=True)
print(f'A ordem decrescente da lista fica assim: {lista}')
print()
print('FIM')
