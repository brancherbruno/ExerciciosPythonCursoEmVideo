exp = str(input('Digite uma expressão matemática: ')).strip().upper()
parea = 0
paref = 0
for v in exp:
    if v == '(':
        parea += 1
    if v == ')':
        paref += 1
print(f'Foram abertos {parea} parênteses.')
print(f'Foram fechados {paref} parênteses.')
if parea == paref:
    print('A expressão digitada está correta.')
else:
    print('A expressão digitada está incorreta.')
