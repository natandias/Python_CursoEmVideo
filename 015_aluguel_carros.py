dias_alugados = int(input("Por quantos dias o carro foi alugado: "))
km_rodados = float(input("Quantos km foram percorridos: "))


preco = km_rodados*0.15 + dias_alugados*60
print (f"O preço total é: R${preco:.2f}")