lista_num = []

while True:    
    r = str(input('Deseja inserir um número na lista?[S/N]: ').strip())
    
    if r not in 'SsNn':
        print('Opção inválida.')

    if r in 'Ss':
        num = int(input('Digite um valor: '))
    
        if num in lista_num:
            print('Este valor já foi adicionado!')
        else:
            print('Valor adicionado com sucesso!')
            lista_num.append(num)

    if r in 'Nn':
        print('Finalizado com sucesso.')
        break

lista_num.sort()
print(f'Lista de números ordenados (crescente): {lista_num}.')
