frase = str(input('Digite uma frase: ')).upper().strip()
print('Nesta frase há: {} letras "A".'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição: {}.'.format(frase.find('A') + 1))
print('A última letra "A" aparace na posição: {}.'.format(frase.rfind('A')))