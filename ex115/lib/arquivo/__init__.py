from ex115.lib.interface import *


def cadastrar_pessoa():
    nome = str(input('Nome: ')).strip()
    idade = leia_int('Idade: ')
    try:
        with open('dados.txt', 'a') as arquivo:
            arquivo.write(str(nome) + '\n')
            arquivo.write(str(idade) + '\n')
        print('Dados salvos com sucesso!')
    except Exception as erro:
        print('ERRO! Não foi possível salvar as informações.')
        print(erro)


def ver_pessoas_cadastradas():
    with open('dados.txt', 'r') as arquivo:
        pessoas = arquivo.readlines()
    for index in range(0, len(pessoas), 2):
        nome = str(pessoas[index].rstrip('\n'))
        idade = str(pessoas[index + 1]).rstrip('\n')
        print(f'{nome:34}{idade:>3} anos')
    linha()