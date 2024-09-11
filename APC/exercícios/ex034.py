s = float(input('Qual o valor do salário?: '))
if s <= 1250:
    sr = s + (s * 0.15)
    print('O salário de: R${:.2f}. Foi reajustado para: R${:.2f}.'.format(s, sr))
else:
    sr = s + (s * 0.1)
    print('O salário de: R${:.2f}. Foi reajustado para: R${:.2f}.'.format(s, sr))
