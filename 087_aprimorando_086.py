matriz = [[], [], []]
soma_pares = soma_terceira_coluna = maior_sl = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append((int(input(f"Digite um valor para a posição {[l, c]}: "))))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

for c in range(0, 3):
    soma_terceira_coluna += matriz[c][2]
    if matriz[1][c] > maior_sl:
        maior_sl = matriz[1][c]

print("\n")
for i in range(0, 3):
    print("|", end=' ') 
    for k in range(0, 3):    
        print (f"{matriz[i][k]:^5}",end=' ')
    print("|") 
print("\n")
print("A soma dos pares é igual a", soma_pares)
print("A soma da terceira coluna é", soma_terceira_coluna)
print("O maior valor da segunda linha é", maior_sl)
