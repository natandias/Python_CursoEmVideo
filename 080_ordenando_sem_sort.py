print("==Você irá digitar cinco valores==")
lista = []
for i in range(0, 5):
    k = i
    valor = int(input(f"\nDigite o {i} valor: "))
    if i == 0:
        lista.append(valor)
        print("O valor foi adicionado ao início da lista")
    elif valor < lista[i-1]:
        while valor < lista[k-1]:
            k = k-1
            if k == 0:
                lista.insert(k, valor)
                print(f"O valor foi adicionado à posição {k} da lista")
                break
            elif valor >= lista[k-1]:
                lista.insert(k, valor)
                print(f"O valor foi adicionado à posição {k} da lista")
                break
    else:
        lista.append(valor)
        print("O valor foi adicionado ao final da lista")

print("\nOs valores digitados em ordem crescente foram:", lista)
