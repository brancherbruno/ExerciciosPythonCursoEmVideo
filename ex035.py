print('=-='*25)
nome = str(input('Qual seu nome?')).upper().strip()
r1 = int(input('{} digite o tamanho da primeira reta:'.format(nome)))
r2 = int(input('{} digite agora o valor da segunda reta:'.format(nome)))
r3 = int(input('Digite o último valor de reta:'))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('{} os valores de reta que você digitou podem formar um triângulo!'.format(nome))
else:
    print('{} infelizmente os valores de retas digitados não podem formar um triângulo!'.format(nome))
prit('=-='*25)