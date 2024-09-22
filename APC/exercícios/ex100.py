from random import randint

def sorteia():
    global list_num
    list_num = []
    n = 0
    for i in range(5):
        n  = randint(0, 10)
        list_num.append(n)
    print(list_num)


def somapar():
    somap = 0
    for i in list_num:
        if i % 2 == 0:
            somap += i
    print(f'A soma dos números pares na lista: {list_num} é igual a: {somap}.')


#PROGRAMA PRINCIPAL
# sorteia()
# somapar()


#POR OUTRO MODO:
def sorteia2(list):
    for i in range(5):
        list.append(randint(0, 10))


def somaPar(list):
    somap = 0
    for i in list:
        if i % 2 == 0:
            somap += i
    print(f'Soma dos pares na lista: {list}, é igual a: {somap}')


numeros = []
sorteia2(numeros)
print(numeros)
somaPar(numeros)
