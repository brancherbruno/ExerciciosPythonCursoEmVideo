from time import sleep
print('\033[1;36m[=]\033[m'*35)
nome = str(input('Olá, qual seu nome?')).capitalize().strip()
peso = float(input('\033[34m{}\033[m por favor digite seu peso agora:'.format(nome)))
alt = float(input('\033[34m{}\033[m digite sua altura agora (altura em m):'.format(nome)))
imc = peso/(alt**2)
print('\033[1;32mAguarde, calculando seu IMC...\033[m')
sleep(4)
print('\033[34m{}\033[m seu IMC é: {:.2f}'.format(nome, imc))
print('\033[1;32mAguarde, verificando seu peso ideal...\033[m')
sleep(3)
if imc < 18.5:
    print('Seu IMC está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está em seu peso ideal!')
elif 25 <= imc < 30:
    print('Voê está em sobrepeso! Precisa perder alguns kg.')
elif 30 <= imc < 40:
    print('\033[33mVocê está com obesidade! Cuidado com sua saúde!\033[m')
elif imc >= 40:
    print('\033[31mVocê está com obesidade mórbida! Procure urgente um médico!\033[m')
print('\033[1;36m[=]\033[m'*35)
