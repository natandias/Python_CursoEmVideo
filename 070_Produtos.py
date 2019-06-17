total = 0.00
mais_de_1000 = 0

while 1:
    print("\n")
    print("*"*15, "PDV", "*"*15)
    nome_pdto = str(input("Nome do produto: "))

    preco_pdto = float(input("Preço: R$ "))
    if preco_pdto > 1000:
        mais_de_1000 += 1

    if total == 0.00:
        menor_preco = preco_pdto
        nome_mais_barato = nome_pdto

    elif preco_pdto < menor_preco:
        menor_preco = preco_pdto
        nome_mais_barato = nome_pdto

    qtd_pdto = int(input("Quantas unidades: "))
    while qtd_pdto == 0:
        qtd_pdto = int(input("Quantidade deve ser superior a 0: "))

    total += preco_pdto * qtd_pdto

    continuar = str(input("Deseja continuar[S/N]? ")).upper().strip()
    while continuar not in "SN":
        continuar = str(input("Deseja continuar[S/N]? ")).upper().strip()
    if continuar == 'N':
        break

print("\n")
print(f"Total Gasto: R${total:.2f}")
print(f"Quantos produtos mais caros que R$1000: {mais_de_1000}")
print(f"O produto mais barato foi: {nome_mais_barato} e custou R$ {menor_preco:.2f}")
print("\n")
