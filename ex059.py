from time import sleep
nome = str(input('Digite sue nome: ')).strip().capitalize()
n1 = int(input('{} digite um número: '.format(nome)))
n2 = int(input('{} digite outro número: '.format(nome)))
es = 0
while es != '5':
    print('\n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Trocar os números \n [5] Sair do programa \n')
    es = str(input('-->Qual sua escolha {}? '.format(nome)))

    if es == '1':
        sleep(1)
        print('\n{} a soma de {} com {} é {}.'.format(nome, n1, n2, n1+n2))
    elif es == '2':
        sleep(1)
        print('\n{} a multiplicação de {} e {} é {}'.format(nome, n1, n2, n1*n2))
    elif es == '3':
        if n1 > n2:
            sleep(1)
            print('\n{} o maior número é {}.'.format(nome, n1))
        else:
            sleep(1)
            print('\n{} o maior número é {}.'.format(nome, n2))
    elif es == '4':
        sleep(1)
        n1 = int(input('\n{} digite um outro valor: '.format(nome)))
        n2 = int(input('{} digite um segundo outro valor: '.format(nome)))
    elif es > '5':
        sleep(2)
        print('\nOpção inválida {}, por favor tente novamente!'.format(nome))
    print('=:='*10)
sleep(3)
print('\nObrigado por utilizar meu programa.')
print('=:='*10)
