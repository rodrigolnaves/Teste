def cor(cor_escolhida):
    cores = {'vermelho': '\033[1;031m',
             'verde': '\033[1;032m',
             'amarelo': '\033[1;033m',
             'azul': '\033[1;034m',
             'roxo': '\033[1;035m',
             'ciano': '\033[1;036m',
             'limpa': '\033[m'}
    return cores[cor_escolhida]


def pressione_para_continuar():
    input('Pressione [ENTER] para continuar...')


def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except Exception as erro:
            print(f'{cor("vermelho")}ERRO! {erro.__class__}\nDigite um valor inteiro válido.{cor("limpa")}')
    return num


def linha(tam=42):
    print('-' * tam)


def titulo(msg):
    linha()
    print(msg.center(42))
    linha()


def menu(opcoes_do_menu):
    titulo('MENU PRINCIPAL')
    for i, opc in enumerate(opcoes_do_menu):
        print(f'{cor("amarelo")}{i + 1}{cor("limpa")} - {cor("azul")}{opc}{cor("limpa")}')
    linha()
    opcao_escolhida = leia_int(f'{cor("amarelo")}Sua opção: {cor("limpa")}')
    return opcao_escolhida

