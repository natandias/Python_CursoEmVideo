lista = []

while True:
    lista.append(int(input("\nDigite um número: ")))

    continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    if continuar == 'N':
        break

print(f"\nForam digitados {len(lista)} números")

lista.sort(reverse=True)
print(f"Números digitados em ordem decrescente: ", lista)

if 5 in lista:
    print(f"O numero 5 está na lista na posição {lista.index(5)}")
else:
    print("O número 5 não foi encontrado na lista")
print("\n")
