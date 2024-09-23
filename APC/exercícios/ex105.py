def notas(*n, sit=False):
    """
    -> Função para analisar notas e menções.
    :param n: notas, (quantidade não definida).
    :param sit: valor opcional, indicando se deve ou não mostrar a menção.
    :return: dicionário com notas e menções do aluno.
    """

    r = dict()

    maior = menor = c =  media = 0
    r['quantidade'] = len(n)
    
    for i in n:
        media += i

    media = media / len(n)
    r['media'] = media

    for i in n:
        if c == 0:
            maior = menor = i
        else:
            if i > maior:
                maior = i
            elif i < menor:
                menor = i
        c += 1
    r['maiornota'] = maior
    r['menornota'] = menor

    if sit:
        if r['media'] < 5:
            r['sit'] = 'MI'
        elif r['media'] >= 5 and r['media'] < 7:
            r['sit'] = 'MM'
        elif r['media'] >= 7 and r['media'] < 9:
            r['sit'] = 'MS'
        elif r['media'] >= 9 and r['media'] <= 10:
            r['sit'] = 'SS'

    return r


#PROGRAMA PRINCIPAL
print(notas(5, 3, 2, sit=True))
print(notas(9, 7, 6, sit=True))
help(notas)
