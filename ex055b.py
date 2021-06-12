pma = 0
pme = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa em kg: '.format(pessoa)))
    if pessoa == 1:
        pma = peso
        pme = peso
    else:
        if peso > pma:
            pma = peso
        if peso < pme:
            pme = peso
print('O maior peso digitado foi {:.2f}'.format(pma))
print('O menor peso digitado foi {:.2f}'.format(pme))
