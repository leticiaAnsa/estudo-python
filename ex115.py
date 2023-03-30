from interface import *
from interface import menu
from time import sleep


arq = 'cursoemvídeo.txt'

if arquivoExiste(arq):
    criarArquivo(arq)

while True:

    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        sleep(2)
        'Gustavo 21'
        'Leticia 12'

        #Opção de listar o conteúdo de um arquivo!
    elif resposta == 2:
        cabeçario('Opção 2')
        cabeçario('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçario('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
        sleep(2)










#Crie um pequeno sistema modularizado que permita
#cadastrar pessoas pelo seu nome e idade em um arquivo
#de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa
#e listartodas as pessoas cadastradas.

#print('-' * 39)
#print('         MENU PRINCIPAL')
#print('-' * 39)
#o1 = print('1- Ver pessoas cadastradas')
#o2 = print('2- Cadastrar nova pessoa')
#o3 = print('3- Sair do sistema')
#print('-' * 39)
#opção = input('Que opção você escolheu: ')
#if opção == '1':

#if opção == '2':
#    nome = input('Nome: ')
#    print(f'''     {nome}
#    Larissa
#    Cibele
#    Heitor
#    Vaunir
#    João Pedro
#    Davi Lucca
#    Ana Leticia
#    ''')

#if opção == '3':
#    print('Ok, até a próxima')
