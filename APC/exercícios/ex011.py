b = float(input('Qual a largura da parede?: '))
h = float(input('Qual a altura da parede?: '))
A = (b * h)
qtdeTinta = (A / 2)
print('Esta parede com dimensão {:.2f}x{:.2f} tem área {:.2f}m².'.format(b, h, A))
print('Para pintar esta parede precisará de {:.2f}l de tinta.'.format(qtdeTinta))