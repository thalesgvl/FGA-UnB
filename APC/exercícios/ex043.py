h = float(input('Qual a sua altura?(m): '))
m = float(input('Qual o seu peso?(kg): '))
imc = (m / (h ** 2))

if imc < 18.5:
    print('IMC: {:.1f}. Abaixo do peso ideal.'.format(imc))
elif imc <= 25:
    print('IMC: {:.1f}. Peso ideal.'.format(imc))
elif imc <= 30:
    print('IMC: {:.1f}. Sobrepeso.'.format(imc))
elif imc <= 40:
    print('IMC: {:.1f}. Obesidade'.format(imc))
else:
    print('IMC: {:.1f}. Obesidade mórbida.'.format(imc))
