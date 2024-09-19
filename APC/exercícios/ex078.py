lista_num = []
maior = 0
menor = 0
i_maior = 0
i_menor = 0

for i in range(5):
    num = int(input(f'Digite um valor para posição [{i}] : '))
    lista_num.append(num)

for i, n in enumerate(lista_num):
    if i == 0:
        maior = menor = lista_num[0]
    else:

        if n > maior:
            maior = n
            i_maior = i

        if n < menor:
            menor = n
            i_menor = i

print('=-' * 30)
print(f'Lista de números: {lista_num}')
lista_num.sort()
print(f'Lista de números enumerada (crescente): {lista_num}')
lista_num.sort(reverse=True)
print(f'Lista de números enumerada (decrescente): {lista_num}')
print('=-' * 30)
print(f'O maior valor encontrado foi: {maior}, na posição: {i_maior}. O menor valor encontrado foi: {menor}, na posição: {i_menor}.')
