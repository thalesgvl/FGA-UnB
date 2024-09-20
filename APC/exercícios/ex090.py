aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno(a): '))
aluno['media'] = float(input('Digite a média do aluno(a): '))

if aluno['media'] < 5:
    aluno['mencao'] = 'MI'

elif aluno['media'] >= 5 and aluno['media'] < 9:
    aluno['mencao'] = 'MM'

elif aluno['media'] >= 9:
    aluno['mencao']  = 'SS'

print('-=' * 15)

for k, v in aluno.items():
    print(f'   - {k} é igual a: {v}.')

print('-=' * 15)
