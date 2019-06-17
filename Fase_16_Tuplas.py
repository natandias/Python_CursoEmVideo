''' TUPLAS SÃO IMUTÁVEIS E ACEITAM DADOS DE TIPOS DIFERENTES'''


'''Criando Tupla lanche:'''
# Tupla pode ser escrita entre parenteses:
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
# Ou não:
# lanche = "Hamburguer", "Suco", "Pizza", "Pudim"

print(lanche)  # printa toda a tupla
print("\n")
print(lanche[1:3])  # printa elemento da posição referenciada entre colchetes
# [-] posição negativa: conta de trás para frente
# [1:3] do elemento da posição 1 até elemento da posição 2 (ignora o 3)
# [1:] do elemento da posição 1 até o final
# [:2] do primeiro elemento até elemento da posição 1 (ignora o 2)
# [-3:] do elemento da posição -3 até o úlimo elemento

''' perceba que não é possível alterar elementos depois de declarados: '''
# lanche[1] = "soda"
print("\n")

''' len retorna o tamanho (qtd de elementos) da tupla: '''
print(f"Comprimento da tupla lanche: {len(lanche)}")
print("\n")

''' Printando de forma organizada: '''
# 1ª maneira
for comida in lanche:
    print(comida)
print("\n")
# 2 ª maneira
for i in range(0, len(lanche)):
    print(lanche[i])
print("\n")
# 3ª maneira (enumerate() retorna contador e variavel[contador]) '''
for cont, comida in enumerate(lanche):
    print(f"O(a) {comida} está na posição {cont}")
print("\n")

'''é possível ordenar a 'tuple' usando a função sorted
mas a função retorna uma lista'''

eat = sorted(lanche)
print(eat)
print(type(eat))

print("\n")
''' se você possui duas tuplas e faz a soma da duas, o retorno são as duas concatenadas '''
# ex:
tuplaA = (2, 3, 5, 7)
tuplaB = (5, 6, 18)
tuplaC = tuplaA + tuplaB
print("TuplaA + TublaB =", tuplaC)

''' Retornar quantos elementos se repetem na tupla'''
print(tuplaC.count(5))

''' Retornar a posição de determinado elemento '''
print(tuplaC.index(18))

''' Tupla com tipos diferentes de dados: '''
pessoa = ('Joao', 40, 'M', 70)
# pode-se usar a função del(variavel) para eliminar variavel após declaração
