t = ('python', 'programar', 'estudar', 'analisar', 'implementar', 'testar', 'programador', 'linguagem', 'praticar')
vogal = ('a', 'e', 'i', 'o', 'u')
for p in t:
    print('\nA palavra: {}. Possui as vogais:'.format(p.upper()),end=' ')
    for letra in p:
        if letra.lower() in vogal:
            print(letra, end=' ')