n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Menu de operações: 
    [1] Somar.
    [2] Multiplicar.
    [3] Maior.
    [4] Novos números.
    [5] Finalizar programa.''')

    opcao = int(input('Qual a opção desejada?: '))

    if opcao == 1:
        print('A soma entre: {} e {} vale: {}.'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('A multiplicação entre: {} e {} vale: {}.'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            print('O maior entre: {} e {} é: {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior entre: {} e {} é: {}.'.format(n1, n2, n2))    
        else:
            print('Os valores: {} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        print('Digite os novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Programa finalizado com sucesso. Volte sempre!')
    else:
        print('Opção inválida. Tente novamente.')