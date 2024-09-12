casa = float(input('Valor do imóvel: '))
salario = float(input('Salário do comprador: '))
ano = int(input('Quantos anos de financiamento? '))

prest = casa / (ano * 12)
min = salario * 0.3

if prest <= min:
    print('O financiamento do imóvel de valor: R${:.2f}. A prestação será de: R${:.2f}, por {} anos.'.format(casa, prest, ano))
    print('\033[32mEmpréstimo concedido!\033[m')
else:
    
    print('O financiamento do imóvel de valor: R${:.2f}. A prestação será de: R${:.2f}, por {} anos.'.format(casa, prest, ano))
    print('\033[31mEmpréstimo não pode ser concedido.\033[m')
