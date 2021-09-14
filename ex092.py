from time import sleep
from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = str(input('Digite o nome do funcionário: ')).strip().capitalize()
dados['idade'] = 0
for i in dados:
    idade = int(input('Digite o ano do nascimento [AAAA]: '))
    dados['idade'] = ano - idade
    break
dados['ctps'] = int(input('Digite o número da CTPS (0 para sem CTPS): '))
if dados['ctps'] != 0:
    cont = int(input('Digite o ano da contratação [AAAA]: '))
    dados['inicio'] = cont
    dados['apose'] = ((35 - (ano - cont)) + (ano - idade))
    dados['salario'] = float(input('Digite o salário: R$ '))
    dados['anoapose'] = ((35 - (ano - cont)) + ano)
else:
    dados['contratacao'] = 35
print('')
print('='*40)
sleep(1.7)
print(f'O nome do cadastro é {dados["nome"]}.')
sleep(1.7)
print(f'A idade de {dados["nome"]} é {dados["idade"]} anos.')
sleep(1.7)
print(f'O número da CTPS de {dados["nome"]} é {dados["ctps"]}.')
sleep(1.7)
if dados['ctps'] != 0:
    print(f'O ano de contratação de {dados["nome"]} foi em {dados["inicio"]}.')
    sleep(1.7)
    print(f'O salário de {dados["nome"]} é de {dados["salario"]}')
    sleep(1.7)
    print(f'A aposentadoria de {dados["nome"]} será em {dados["anoapose"]} com {dados["apose"]} anos.')
print('='*40)
sleep(1.7)
print('='*11, 'FIM DO PROGRAMA', '='*12)
