aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).strip().capitalize()
aluno['media'] = float(input(f'Insira a média do aluno {aluno["nome"]}: '))
print(f'O nome do aluno é: {aluno["nome"]}.')
print(f'A média do aluno é: {aluno["media"]}.')
if aluno['media'] < 5:
    print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e por isso reprovou.')
elif 7 > aluno['media'] >= 5:
    print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e está em recuperação.')
else:
    print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e está aprovado.')
