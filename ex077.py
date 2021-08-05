palavras = ('carro', 'baleia', 'arara', 'hospital', 'elefante', 'Renata', 'Bruno')
print('QUAIS AS VOGAIS DAS FRASES?')
print('-'*30)
for frase in palavras:
    print(f'\nNa palavra {frase} temos:', end=' ')
    for letra in frase:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
print('-'*30)
print('FIM')
