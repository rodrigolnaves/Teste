from ex115.lib.arquivo import *
from time import sleep

opcoes_do_menu = ['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA']

while True:
    opcao_escolhida = menu(opcoes_do_menu)
    print('\n' * 60)
    if opcao_escolhida == 1:
        titulo('PESSOAS CADASTRADAS')
        ver_pessoas_cadastradas()
        pressione_para_continuar()
    elif opcao_escolhida == 2:
        titulo('CADASTRAR PESSOA')
        cadastrar_pessoa()
        pressione_para_continuar()

    elif opcao_escolhida == 3:
        titulo('SAINDO DO SISTEMA')
        break
    else:
        print(f'{cor("vermelho")}ERRO! Escolha uma opção válida.{cor("limpa")}')
    sleep(0.5)
    print('\n' * 60)
