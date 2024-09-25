def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('Erro. Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n
        

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('Erro. Digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n
        

n1 = leiaInt()
n2 = leiaFloat()

print(f'Valor inteiro: {n1}\nValor real: {n2}.')