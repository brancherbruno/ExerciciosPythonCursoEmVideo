from time import sleep
dados = {}
gols = []
total = 0
print('')
print('-='*15, 'ESTATÍSTICAS DO JOGADOR', '-='*15)
sleep(1.5)
print('')
dados['nome'] = str(input('Digite o nome do jogador: ')).strip().capitalize()
sleep(0.6)
print('')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
sleep(0.6)
print('')
for g in range(partidas):
    gols.append(int(input(f'Quantos gols {dados["nome"]} fez na partida {g+1}? ')))
    sleep(0.6)
for gol in gols:
    total += gol
dados['partidas'] = partidas
dados['gols'] = gols
dados['total'] = total
print('')
print('-='*15, 'AGUARDE, PROCESSANDO AS ESTATÍSTICAS', '-='*15)
sleep(1.5)
print('')
print(f'O jogador {dados["nome"]} fez {dados["total"]} gols em {dados["partidas"]} partidas.')
sleep(1)
print('')
for g in range(partidas):
    print(f'{"=>":<4} Na partida {g+1} {dados["nome"]} fez {dados["gols"][g]} gols.')
print('')
print('-='*15, 'FIM DO PROGRAMA', '-='*15)
