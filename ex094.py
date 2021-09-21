dados = {}
dadost = []
soma = media = 0
while True:
    dados['nome'] = str(input('Digite o nome: ')).strip().title()
    dados['idade'] = int(input(f'Digite a idade de {dados["nome"]}: '))
    soma += dados['idade']
    dados['sexo'] = str(input(f'Digite o sexo de {dados["nome"]} [M/F] ')).strip().capitalize()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input(f'Erro de digitação. Por favor, utilize somente M ou F. Qual o sexo de {dados["nome"]}: ')).strip().capitalize()[0]
    dadost.append(dados.copy())
    dados.clear()
    while True:
        sair = str(input('Deseja continuar o cadastro? [S/N] ')).strip().capitalize()[0]
        if sair in 'SN':
            break
        print('Erro de digitação, por favor digite apenas S ou N:')
    if sair == 'N':
        break
print(dadost)
print(f'A) Foram cadastradas {len(dadost)} pessoas.')
media = soma / len(dadost)
print(f'B) A idade média das pessoas cadastradas é {media:.2f} anos')
print('C) As mulheres cadastradas foram: ', end='')
for i in dadost:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')
print()
print('As pessoas com idade maior que a média são: ', end='')
for v in dadost:
    if v['idade'] > media:
        print(f'{v["nome"]} ', end='')
