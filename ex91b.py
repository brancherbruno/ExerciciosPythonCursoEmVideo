#importar o randint para randomizar os valores de dados
#importar time para dar o tempo entre as acoes
#importar iteemgetter para poder colocar em ordem a biblioteca dentro da lista
from random import randint
from time import sleep
from operator import itemgetter
#biblioteca e lista em branco para serem preenchidas
jogadores = {}
jogo = []
while True:
    #comando para digitar quantos jogadores quiserem
    sair = ' '
    jogadores['Jogador'] = str(input('Digite o nome do primeiro jogador: ')).strip().capitalize()
    print(f'{jogadores["Jogador"]} aguarde enquanto seu número é sorteado...')
    sleep(2)
    #comando para randomizar o valor sorteado do dado
    jogadores['dado'] = randint(1, 6)
    #comando para jogar os valores da biblioteca dentro da lista
    jogo.append(jogadores.copy())
    #comando para decisao de sair
    while sair not in 'SN':
        sair = str(input('Você gostaria de adicionar mais um jogador?[S/N] ')).strip().capitalize()[0]
    if sair == 'N':
        break
print('')
print('#'*60)
#fazer mais uma biblioteca para poder colocar em ordem
ranking = []
print('AGUARDE.....')
print('#'*60)
sleep(3)
#comando para impressão do valores gerados automaticamente
for i in jogo:
    print(f'O jogador {i["Jogador"]} tirou o número {i["dado"]}.')
print('')
print('#'*60)
print('')
print('Aguarde, estamos verificando os vencedores...')
sleep(2)
#comando para colocar em ordem os valores da lista
ranking = sorted(jogo, key=itemgetter('dado'), reverse=True)
print('')
print('#'*60)
sleep(3)
#comando para fazer a impressao mais ou menos formatada...kkkk mas ja fica bonito de ver
for l, v in enumerate(ranking):
    print(f'{l+1} lugar: {v["Jogador"]} com o número {v["dado"]}')
print('#'*60)
sleep(2)
print('='*20, 'FIM DE JOGO', '='*20)
