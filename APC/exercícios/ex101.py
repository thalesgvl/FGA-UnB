
def voto(ano_nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nasc

    if idade < 16:
        return print(f'IDADE: {idade}. VOTO NEGADO.')
    
    elif 16 <= idade < 18 or idade > 65:
        return print(f'IDADE: {idade}. VOTO OPCIONAL.')

    else:
        return print(f'IDADE: {idade}.  VOTO OBRIGATÓRIO.')


#PROGRAMA PRINCIPAL
voto(2002)
voto(1950)
voto(2009)
