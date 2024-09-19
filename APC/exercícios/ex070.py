tot = v_1000 = c = 0
menor_v = 0
n_menorv = 0
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if r =='S' or  r == 'N':
        c += 1
        tot += valor
        if valor > 1000:
            v_1000 += 1
        if c == 1:
            menor_v = valor
            n_menorv = nome
        else:
            if valor < menor_v:
                menor_v = valor
                n_menorv = nome
            if r =='N':
                break
    else:
        print('Resposta inválida. Tente novamente.')
print('{:-^40}'.format(' Fim do programa. '))
print('O total da compra foi de: R${:.2f}.'.format(tot))
print('Temos: {} produto(s) custando mais de: R$1000.00.'.format(v_1000))
print('O produto mais barato foi: {}. Custando: R${:.2f}.'.format(n_menorv, menor_v))
