from random import shuffle

lista = []

for i in range(4):
    n = str(input('Digite o nome dos (04) alunos: '))
    n = lista.append([n])
shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))