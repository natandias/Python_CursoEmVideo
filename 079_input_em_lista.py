lista = []
while True:
    valor = int(input("\nDIgite um valor númerico: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor não foi adicionado, pois já está na lista")

    continuar = str(input("Deseja cadastrar mais numeros[S/N]?: ")).strip().upper()
    while continuar not in 'SN':
        continuar = str(input("Deseja cadastrar mais numeros[S/N]?: ")).strip().upper()
    if continuar == 'N':
        print("\n")
        break
   
print("Esses foram os valores que você digitou, em ordem crescente: ")
lista.sort()
for i in lista:
    print(i, end='  ')
print("\n")
