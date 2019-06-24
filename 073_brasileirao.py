tabela = ("Palmeiras", "Santos", "Flamengo", "Internacional", "Atletico-MG",
          "Goias", "Botafogo",  "Bahia", "Sao Paulo", "Corinthians", "Gremio",
          "Athletico-PR", "Ceara", "Fortaleza", "Vasco", "Fluminense",
          "Chapecoense", "Cruzeiro", "CSA", "Avai")

print("\nTABELA DO BRASILEIRÃO: ")
for i, times in enumerate(tabela):
    i += 1
    print(f"{i}. {times}")

print("\nCinco primeiros colocados:")
for i in range(0, 5):
    print(tabela[i], end="  ")
print("\n")
# ou print(tabela[0:5])

print("Últimos quatro colocados:")
for i in range(-4, 0):
    print(tabela[i], end="  ")
print("\n")
# ou print(tabela[-4:])

print("Times em ordem alfabética:")
tabela_ord_alfab = sorted(tabela)
for times in tabela_ord_alfab:
    print(times)
print("\n")

pesq = str(input("Deseja saber a posição de qual time: ")).strip().capitalize()
if pesq not in tabela:
    print(f"{pesq} não existe ou não está na série A do Brasileirão\n")
else:
    print(f"{pesq} está na posição: {tabela.index(pesq)+1}\n")
