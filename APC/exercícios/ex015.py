dias = int(input('Quantos dias foram alugados?: '))
dist = float(input('Quantos km foram percorridos?: '))
valor = (110 * dias + 0.5 * dist + 70)
print('O total a pagar por {} dia(s) alugado(s) e distância percorrida de: {:.2f}km é de: R${:.2f}.'.format(dias, dist, valor))