from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 10))


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos numeros pares dessa lista é {soma}")


ls = []
print()
sorteia(ls)
print('Lista: ', ls)
somaPar(ls)
print()
