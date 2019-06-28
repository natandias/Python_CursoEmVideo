''' Dicionários são listas com indíces nominais '''
# tuplas = ()
# listas = []

''' Iniciando dicionários '''
# dicionarios = {}
# dicionarios = dict()

''' Iniciando dicionarios com valores '''
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])

''' Adicionando novas chaves ao dicionario '''
dados['sexo'] = 'M'
# append não funciona em dicionário

''' Apagando elementos em dicionário '''
del dados['idade']
print(dados)

''' Partes do Dicionário '''
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
# values -> valores que estão dentro das chaves
# keys -> os 'indices' do dicionario
# items -> chaves e respectivos valores formam os itens
print(filme.values())
print(filme.keys())
print(filme.items())
print()

''' Printando items do dicionário '''
for k, v in filme.items():
    print(f'O {k} do filme é {v} ')

''' Inserindo dicionario em lista '''
locadora = []
locadora.append(filme)
print(locadora[0]['ano'])
print()

''' Inserindo dicionario em lista com FOR '''
# use o método .copy() para passar um dicionário para uma lista
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# printando:
for i in brasil:
    for k, v in i.items():
        print(f'Campo {k} = {v} ')
