# Listas podem ser alteradas diferentemente das tuplas
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

''' Pode-se trocar um elemento realizando atribuição '''
lanche[3] = 'goiabada'
print(lanche)

''' Adicionando valor à lista '''
lanche.append('biscoito')
print(lanche)

''' Adicionando valor entre elementos da lista '''
lanche.insert(0, 'Ice Cream')
print(lanche)

''' Apagando elemento '''
del lanche[3]
print(lanche)

''' Usando método POP '''
lanche.pop(3)
print(lanche)
# utilizando pop sem parametro, é eliminado o último elemento da lista

''' Usando remove (indica-se valor a ser removido) '''
lanche.remove('biscoito')
print(lanche)
# se houver dois valores iguais, irá remover o primeiro

''' Se tentar remover um valor que não está na lista o programa dá erro
        pode - se usar uma estrutura de controle para evitar esse problema
'''
if 'suco' in lanche:
    lanche.remove('suco')
print(lanche)

''' Pode-se criar lista de duas formas '''
p = []
q = list()


''' Criando lista com valores consecutivos (usando list) '''
valores = list(range(4, 11))
print(valores)

''' Ordenando lista em ordem crescente '''
non_ordered = [8, 2, 5, 4, 9, 3, 0]
non_ordered.sort()
print(non_ordered)

''' Ordenando lista em ordem decrescente '''
non_ordered = [8, 2, 5, 4, 9, 3, 0]
non_ordered.sort(reverse=True)
print(non_ordered)

''' Quantos elementos uma lista possui? '''
size = len(non_ordered)
print(size, 'elementos')

print("\n")
''' Print organizado '''
v = []
v.append(5)
v.append(9)
v.append(4)

for c, elm in enumerate(v):
    print(f'Na posição {c} encontrei o valor {elm}')
print('Fim da Lista\n')

''' Lendo valores digitados pelo usuario '''
for cont in range(0, 2):
    v.append(int(input("Digite um valor: ")))

for c, elm in enumerate(v):
    print(f'Na posição {c} encontrei o valor {elm}')
print('Fim da Lista')

''' Se a uma lista recebe outra, ela irá receber os endereços de mémoria
    e não os valores, ou seja, se uma valor é alterado na segunda lista,
    ele também é alterado na lista original '''
a = [1, 2, 3, 4]
b = a
print('\nLista A: ', a)
print('Lista B: ', b)
b[2] = 10
print('Lista A depois que Lista B foi alterada: ', a)

''' Copiando todos os elementos de uma lista para outra '''
b = a[:]
b[2] = 5
print('Lista A depois que B foi alterada:', a)
# perceba que os valores da lista A não se alteram

print("\nFIM DA AULA")
