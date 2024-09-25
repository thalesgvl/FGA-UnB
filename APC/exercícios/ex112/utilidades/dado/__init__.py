def leiaDinheiro():
    valido = True
    while valido:
        p = input('Digite um valor: R$').replace(',', '.').strip()
        if (p.isalpha()) or (p.isspace()):
            print('Entrada inválida, insira um valor.')
        
        else:
            valido = False
            return float(p)