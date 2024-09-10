v = float(input('Qual a velocidade atual do carro em km/h?: '))

if v <= 80:
    print('\033[0;32mTenha um bom dia! Dirija em segurança.\033[m')
else:
    print('\033[0;31mVocê foi multado. Excedeu a velocidade máxima em:\033[m\033[0;33m {:.2f}km/h.\033[m'.format(v - 80))
    print('\033[0;31mO valor da multa é de:\033[m \033[0;33mR${:.2f}.\033[m'.format((v - 80) * 7))
