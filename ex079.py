nome = str(input('Digite seu nome: ')).strip().capitalize()
valor = []
while True:
    #de vazio é para decisão de continuar no final do programa
    de = ' '
    es = int(input(f'{nome} digite um valor: '))
    #primeiro SE, caso o valor não esteja na lista, ele adiciona o valor
    if es not in valor:
        valor.append(es)
    #mas caso ele já esteja na lista, vai aparecer essa frase:
    elif es in valor:
        print(f'{nome} esse valor já consta na lista. Por favor escolha outro.')
    #pergunta se quer continuar a adicionar valores na lista
    while de not in 'SN':
        de = str(input(f'{nome} gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if de == 'N':
        break
valor.sort()
print(valor)
