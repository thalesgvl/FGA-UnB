temp = []
lista_pessoas = []
maior = menor = 0

while True:

    nome = str(input('Digite seu nome: '))
    temp.append(nome)
    peso = float(input('Digite seu peso: '))
    temp.append(peso)
    

    if len(lista_pessoas) == 0:
        maior = menor = temp[1]

    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    lista_pessoas.append(temp[:])

    temp.clear()

    r = str(input('Deseja continuar[S/N]?: '))

   
    if r in 'Nn':
        break

print(f'Foram regristradas: {len(lista_pessoas)} pessoas.')
print(f'O menor peso regristrado foi: {menor} e o maior foi: {maior}.')
for i in lista_pessoas:
    if i[1] == maior:
        print(f'O maior peso foi de {maior}. Peso do(a): {i[0]}.')
    if i[1] == menor:
        print(f'O menor peso foi de {menor}. Peso do(a): {i[0]}.')

