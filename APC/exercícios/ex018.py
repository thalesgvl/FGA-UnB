from math import radians, sin, cos, tan
an = float(input('Qual o valor do ângulo?: '))
sen = sin(radians(an))
cos = cos(radians(an))
tg = tan(radians(an))
print('O ângulo {:.2f} possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(an, sen, cos, tg))
