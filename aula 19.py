#filme = {'titulo': 'Star wars',
#'ano':1977,
#'diretor':'Jorge lucas'}

#for k,v in filme.items():
#    print(f'O {k} é {v}')


#pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade':22}
#print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')


#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'Idade': 22}
#pessoas['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
#print(pessoas.items())
#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#brasil = list()
#estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)


#print(brasil[1]['sigla'])




estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    #for k, v in e.items():
    #    print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
        print()


