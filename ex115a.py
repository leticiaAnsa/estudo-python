from interface import *
from interface import menu
from time import sleep


while True:

    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçario('Opção 1', 'vermelho')
    elif resposta == 2:
        cabeçario('Opção 2')
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
#    print('''    Larissa
#    Cibele
#    Heitor
#    Vaunir
#    João Pedro
#    Davi Lucca
#    Ana Leticia
#    ''')

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


