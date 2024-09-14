s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos: {:.2f}, {:.2f} e {:.2f}. \033[32mPodem formar triângulo!\033[m'.format(s1, s2, s3))
    if s1 == s2 and s2 == s3:
        print('O triângulo é do tipo: \033[34mEQUILÁTERO.\033[m')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('O triângulo é do tipo: \033[34mISÓSCELES.\033[m')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('O triângulo é do tipo: \033[34mESCALENO.\033[m')
else:
    print('Os segmentos: {:.2f}, {:.2f} e {:.2f}. \033[31mNão podem formar triângulo.\033[m'.format(s1, s2, s3))
