valor = []
for v in range(0, 5):
    n = int(input(f'digite um valor: '))
    #comando para adicionar um valor que não seja repetido
    if v == 0 or n > valor[-1]:
        valor.append(n)
    #comando para calcular o valor e onde ele deve ser colocado na sequencia crescente
    else:
        p = 0
        while p < len(valor):
            if n <= valor[p]:
                valor.insert(p, n)
                break
            p += 1
print(valor)
