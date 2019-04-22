nome = str(input("Digite o nome completo: ").strip())
nome_separado = nome.split()


print(f"Primeiro nome: {nome_separado[0].capitalize()}")
print(f"Último nome: {nome_separado[len(nome_separado)-1].capitalize()} \n")
