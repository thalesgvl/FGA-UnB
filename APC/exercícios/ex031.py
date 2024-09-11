d = float(input('Qual é a distância da viagem (km)?:'))
if d <=200:
    print('Sua viagem de: {:.2f}km. As expensas será de: R${:.2f}.'.format(d, (d * 0.50)))
else:
    print('Sua viagem de: {:.2f}km. É promocional! As expensas será de: R${:.2f}.'.format(d, (d * 0.45)))
