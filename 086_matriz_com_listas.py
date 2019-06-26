matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append((int(input(f"Digite um valor para a posição {[linha, coluna]}: "))))
print("\n")

for linha in range(0, 3):
    print("|", end=' ') 
    for coluna in range(0, 3):   
        print (f"{matriz[linha][coluna]:^5}", end=' ')
    print("|")
print("\n")