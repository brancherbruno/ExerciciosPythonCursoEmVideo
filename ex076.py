lista = ('Pão', 3.50, 'Leite', 4.50, 'Bife', 12.00, 'Salada', 2.50, 'Arroz', 4.00,
         'Feijão', 6.70, 'Batata', 3.75)
print('-'*40)
print(f'{"COMPRAS DO MÊS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>8.2f}')
print('_'*40)
print(f'{"FIM":^40}')
print('_'*40)
