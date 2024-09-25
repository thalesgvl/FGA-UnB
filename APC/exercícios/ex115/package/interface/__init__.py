def mostrarMenu():
        print('-=' * 20)
        print('MENU PRINCIPAL'.center(40))
        print('-=' * 20)
        print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema''')
        print('-=' * 20)

def leiaInt():
    while True:
        try:
            n = int(input('Escolha uma opção: '))
        except (ValueError, TypeError):
            print('Erro. Digite uma opção válida.')
            mostrarMenu()
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


def leiaNome():
    while True:
        try:
            nome = str(input('Nome do usuário: '))
        except(TypeError, ValueError):
            print('Erro, insira um nome válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return nome
        

def leiaIdade():
    while True:
        try:
            n = int(input('Informe a idade: '))
        except (ValueError, TypeError):
            print('Erro. Digite uma opção válida.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n