pma = 0
pme = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        pma = peso
        pme = peso
    else:
        if peso > pma:
            pma = peso
        if peso < pme:
            pme = peso
print('O peso maior é {:.2f}kg'.format(pma))
print('O peso menor é {:.2f}kg'.format(pme))
