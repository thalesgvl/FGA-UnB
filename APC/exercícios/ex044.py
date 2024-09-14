valor = float(input('Valor em compras: '))

print('\033[34mSejam sempre bem-vindos à loja tio patinhas!\033[m')

opcao = int(input('''Opções de pagamento:
\033[33m[1]\033[m À vista (dinheiro/débito).
\033[33m[2]\033[m À vista (crédito).
\033[33m[3]\033[m 2x cartão.
\033[33m[4]\033[m 3x ou mais no cartão.
\033[32mEscolha:\033[m '''))

if opcao == 1:
    print('A compra de: \033[33mR${:.2f}.\033[m Possui desconto, preço final: \033[33mR${:.2f}.\033[m'.format(valor, valor - (valor * 0.1)))
elif opcao == 2:
    print('A compra de: \033[33mR${:.2f}.\033[m Possui desconto, preço final: \033[33mR${:.2f}.\033[m'.format(valor, valor - (valor * 0.05)))
elif opcao == 3:
    print('Preço final: \033[33mR${:.2f}.\033[m'.format(valor))
elif opcao == 4:
    parc = int(input('\033[32mQuantas parcelas?:\033[m '))
    print('A compra de: \033[33mR${:.2f}.\033[m Em será parcelada em {}x de: \033[33mR${:.2f}\033[m, com juros.'.format(valor, parc, (valor + 0.2 * valor) / parc))
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
