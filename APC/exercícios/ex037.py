n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Base Binário.
[2] Base Octal. 
[3] Base Hexadecimal.''')
option = int(input())
if option == 1:
    print('O número: {} na base binária é: {}.'.format(n, bin(n)[2:]))
elif option == 2:
    print('O número: {} na base octal é: {}.'.format(n, oct(n)[2:]))
elif option == 3:
    print('O número: {} na base hexadecimal é: {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')