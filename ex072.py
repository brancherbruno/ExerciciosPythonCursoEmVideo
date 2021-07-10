nome = str(input('Por favor digite seu nome: ')).strip().upper()
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
escolha = ' '
while True:
    c = ' '
    decisao = int(input(f'{nome} digite um número entre 0 e 10: '))
    for escolha in range(0, 11):
        if decisao == escolha:
            print(f'{nome} você digitou o número {num[escolha]}.')
            break
    if decisao != escolha:
        print(f'{nome} você escolheu um valor errado. Tente outra vez.')
    while c not in 'SN':
        c = str(input(f'{nome} você gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Obrigado por utilizar o programa, {nome}.')
print('FIM')
