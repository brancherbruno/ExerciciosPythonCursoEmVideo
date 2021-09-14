from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
joga = []
print('')
print('='*20, 'JOGO DE DADOS', '='*20)
for j in range(0, 4):
        jogadores['jogador'] = f'Jogador{j+1}'
        jogadores['num'] = randint(1, 6)
        joga.append(jogadores.copy())
print('')
ranking = []
for v in joga:
        print('='*31)
        print(f'{v["jogador"]} jogou o dado e saiu {v["num"]}.')
        sleep(2)
print('='*31)
print('')
print('='*20, 'RESULTADO DO JOGO', '='*20)
ranking = sorted(joga, key=itemgetter('num'), reverse=True)
for i, v in enumerate(ranking):
        print(f'{i+1} lugar: {v["jogador"]} que tirou {v["num"]}')
        sleep(2)
