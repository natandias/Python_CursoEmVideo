''' Utilizadas para automatizar o código '''
''' No Python são passados argumentos para as funções '''
''' Tipos complexos são passados por referência (listas, tuplas, etc) '''

#definindo função
def titulo(msg):
    print('-='*20)
    print(msg)
    print('-='*20)

def contador(* num):
    # * num -> forma uma tupla
    # pode-se passar qts parametros quiser
    print(num)

def dobro(lista):
    # dobra valores da lista
    for i in range(0, len(lista)):
        lista[i] *= 2

def soma_lista(lista):
    # soma valores da lista
    soma = 0
    for i in lista:
        soma += i
    print(f"Somando {lista} temos {soma}")

def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f"Somando {valores} temos {soma}")


#chamando função
titulo('alo mundo')

contador(2)
contador(2, 3, 4)
contador(4, 7, 8, 10)

lista = [7, 2, 5, 0, 4]
print("Lista antes de passar na função 'dobro': ", lista)
dobro(lista)
print("Lista depois de passar na função 'dobro': ", lista)

print()
print('Somando Valores individuais:')
soma(5, 2)
soma(2, 9, 4)

print()
print('Somando Lista:')
soma_lista(lista)