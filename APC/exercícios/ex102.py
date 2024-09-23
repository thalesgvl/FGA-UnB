def fatorial(num, show=0):
    """
    -> Calcula o fatorial de um número.
    :param n: O n° a ser calculado.
    :param show: (opcional) Mostrar ou não o procedimento.
    :return: O valor fatorial de um n°.
    """

    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ',end='')
            else:
                print(' = ', end='')
        f *= i
    return f
    
    
#PROGRAMA PRINCIPAL
print(fatorial(5, show=True))
print(fatorial(6))
print(fatorial(9, show=True))
help(fatorial)