print('='*25)
nome = str(input('Olá, qual seu nome?')).upper().strip()
km = int(input('{} por favor digite quantos km você percorreu:'.format(nome)))
t = int(input('{} digite em quanto tempo você percorreu os {}km'.format(nome, km)))
vm = km/t
m = (vm-80)*7.00
if vm > 80:
    print('A velocidade média que você estava era de {}km/h e foi superior a 80km/h, então você foi multado em R${:.2f}!'.format(vm,m))
else:
    print('Parabéns {}, você dirigiu dentro do limite de velocidade!'.format(nome))

print('='*12, 'FIM', '='*12)
