pilha = []

expr = str(input('Digite sua expressão: '))

for i in expr:
    if i == '(':
        pilha.append(i)

    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
    else:
        pilha.append(')')
        break

if len(pilha) != 0:
    print('Expressão incorreta.')
else:
    print('Expressão correta!')
