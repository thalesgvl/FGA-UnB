co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('O triângulo retângulo de cateto oposto {:.2f} e cateto adjacente {:.2f} possui hipotenusa {:.2f}.'.format(co, ca, hip))
