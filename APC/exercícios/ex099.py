def maior(* num):
    maior_num = c = 0
    for n in num:
        if c == 0:
            maior_num = n
        else:
            if n > maior_num:
                maior_num = n
        c += 1
    print(f'\nForam analisados: {c} valores, sendo o maior: {maior_num}.')


#PROGRAMA PRINCIPAL
maior(4, 5, 7, 8)
maior(8, 50, -4, 78, 1, 2, 5, 7)
maior()
maior(-2, -5, 0)
