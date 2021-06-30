c = n = 0
while True:
    print('-'*15)
    n = int(input('Qual tabuada você quer ver?'))
    print('-'*15)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
        c += 1
print('Você digitou um número negativo, oque não é permitido')
print('(o)'*6, 'FIM DO PROGRAMA', '(o)'*6)
