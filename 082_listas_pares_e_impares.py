origin = []
par = []
impar = []

while True:
    origin.append(int(input("\nDigite um numero: ")))

    continuar = str(input("Deseja continuar[S/N]: ")).strip().upper()
    while continuar not in 'SN':
        continuar = str(input("Digite um numero: ")).strip().upper()
    if continuar == 'N':
        break

for num in origin:
    if (num % 2) == 0:
        par.append(num)
    else:
        impar.append(num)

print("\nLista original: ", origin)
print("Lista dos pares: ", par)
print("Lista dos impares: ", impar)
