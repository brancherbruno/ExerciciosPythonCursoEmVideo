#geração de lista vazia
temp = list()
pessoas = list()
gordos = list()
magros = list()
#comando para contagem de pessoas na lista
n = 0
pema = pemo = 0
nome = str(input('Olá usuário, qual seu nome?: ')).strip().capitalize()
#comando para inserir dados
while True:
    d = ' '
    #comando para adicionar informacoes a lista dados
    temp.append(str(input(f'{nome} por favor digite o nome do paciente: ')).strip().capitalize())
    temp.append(int(input(f'{nome} agora digite o peso do paciente: ')))
    #comando de contagem
    n += 1
    #comando para saber se o paciente é magro ou gordo. Primeiro passo é pegar como base o valor de magro, no caso é
    #zero, pois o primeiro paciente vai ser sempre o mais magro ou gordo. Pois é o primeiro paciente.
    if len(pessoas) == 0:
        pema = pemo = temp[1]
    #mas logo em seguida já faz a comparação e joga o paciente pra lista correta, de gordo ou magro.
    else:
        if temp[1] > pemo:
            pemo = temp[1]
        if temp[1] < pema:
            pema = temp[1]
    # nunca esquecer de usar clear, pois se não ele copia os dados em cima dos dados e
    # fica duplicado tudo que tem dentro do das listas
    pessoas.append(temp[:])
    temp.clear()
    #comando de decisao para continuar ou nao a adicao de dados as listas
    if d not in 'SN':
        d = str(input(f'{nome} gostaria de inserir mais dados? [S/N]: ')).strip().capitalize()[0]
    if d == 'N':
        break
#comando para listar o mais gordo e o mais magro - só adiciona o mais gordo e mais
#mais magro, vai adicionair mais se tiverem o mesmo peso
for p in pessoas:
    if p[1] == pemo:
        gordos.append(p[:])
for p in pessoas:
    if p[1] == pema:
        magros.append(p[:])
print('')
print(f'{nome} você cadastrou {n} pacientes.')
print(f'{nome} os pacientes obesos são: {gordos}')
print(f'{nome} os pacientes magros são: {magros}')
#comando para formatacao de impressao
#for i in pessoas:
#    print(f'{i[0]} pesa {i[1]}kg.')
