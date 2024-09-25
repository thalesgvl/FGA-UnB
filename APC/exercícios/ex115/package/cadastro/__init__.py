from package import interface
from package import bd

arq = 'usuarios.txt'
if not bd.arquivoExiste(arq):
    bd.criarArquivo(arq)


def cadastrar():
    while True:
        interface.mostrarMenu()
        opc = interface.leiaInt()
        if opc == 1:
            bd.lerArquivo(arq)
        elif opc == 2:
            pessoa = interface.leiaNome()
            idade = interface.leiaIdade()
            bd.gravarBd(arq, pessoa, idade)
        elif opc == 3:
            print('Sitema finalizado. Volte sempre!')
            break
        else:
            print('Opção inválida. Tente novamente.')