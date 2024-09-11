s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 > s2 - s3 and s1 < s2 + s3:
    print('Os segmentos: {:.2f}, {:.2f} e {:.2f}. Podem formar triângulo!'.format(s1, s2, s3))
else:
    print('Os segmentos: {:.2f}, {:.2f} e {:.2f}. Não podem formar triângulo.'.format(s1, s2, s3))
