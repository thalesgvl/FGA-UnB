dados = []
alunos_notas = []
c = 0

while True:

    nome = str(input('Digite seu nome: '))
    alunos_notas.append(nome)
    p1 = float(input('Digite sua nota da prova 01: '))
    alunos_notas.append(p1)
    p2 = float(input('Digite sua nota da prova 02: '))
    alunos_notas.append(p2)

    media = (p1 + p2) / 2
    alunos_notas.append(media)

    dados.append(alunos_notas[:])
    alunos_notas.clear()

    r = str(input('Deseja inserir outro aluno[S/N]?: '))
    if r in 'Nn':
        break

print('-=' * 15)
print('No.  NOME           MÉDIA')
print('--' * 15)

for i in dados:
    print(f'{c:<5}{i[0]:<15}{i[3]:<3}')
    c += 1


while True:
    print('--' * 15)
    opc = int(input('Deseja mostrar as notas de qual aluno?[999 para finalizar!]: '))
    if opc == 999:
        break
    if opc <= len(dados)-1:
        print(f'Notas de {dados[opc][0]} são: {dados[opc][1]} e {dados[opc][2]}.')

print('Volte sempre.')
