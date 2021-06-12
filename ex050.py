print('\033[1;35m_^_\033[m'*20)
nome = str(input('Digite seu nome:')).capitalize().strip()
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('{} digite o {} valor:'.format(nome, c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('\033[1;36m{}\033[m soma dos {} valores \033[1;31mPARES\033[m digitados é:\033[1;31m{}\033[m'.format(nome, cont, soma))

print('\033[1;35m_^_\033[m'*20)
