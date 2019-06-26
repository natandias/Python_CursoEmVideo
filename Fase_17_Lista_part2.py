''' Listas dentro de listas '''
dados = []
pessoas = list()

dados.append('Pedro')
dados.append(25)
pessoas.append(dados[0:2])

dados.append('Maria')
dados.append(19)
pessoas.append(dados[2:4])

# print(pessoas[1][0])

galera = [['João', 19], ['Ana', 33], ['Joaquim', 80], ['Maria', 45]]
# for p in galera:
# print(f'{p[0]} tem {p[1]} anos de idade')

''' Escaneando valores para uma lista dentro de outra '''
people = []
dado = []
print("\n")
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    people.append(dado[:])
    dado.clear()  # remove todos os dados da lista
print(people)

''' LEMBRE-SE: para copiar dados use [:], pois se não serão
copiados endereços de memória '''

