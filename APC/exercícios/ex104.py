def leiaInt(num):
    while True:
        if num.isnumeric():
            num = int(num)
            return print(f'O valor inserido foi: {num}')
        else:
            print('ERRO. DIGITE UM VALOR INTEIRO.')
            num = str(input('Digite um valor inteiro: '))
    

#PROGRAMA PRINCIPAL
n = str(input('Digite um valor inteiro: '))
leiaInt(n)
