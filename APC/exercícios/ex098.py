from time import sleep



def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    c = inicio
  
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')
        sleep(1.2)
        for i in range(inicio, fim + 1, passo):
            print(f' {i}', end='', flush=True)
            sleep(0.5)
        print(' Fim!')
    
    else:
        print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')
        sleep(1.2)
        while c >= fim:
            print(f' {c}', end='', flush=True)
            sleep(0.5)
            c -= passo
        print(' Fim!')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
