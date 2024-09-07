s = float(input('Qual o salário do funcionário?: '))
sa = (s * 0.15)
novo_s = (s + sa)
print('O salário de: R${:.2f}, com aumento de 15% passa a ser: R${:.2f}.'.format(s, novo_s))
