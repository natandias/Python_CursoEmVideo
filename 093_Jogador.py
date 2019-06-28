jogador = {}
gols = []
tot_gols = 0

jogador['Nome'] = str(input("Nome do jogador: ")).strip()
qtd_partidas = int(input("Ele jogou quantas partidas? "))
for i in range(0, qtd_partidas):
    gols.append(int(input(f"Quantos gols fez na partida {i+1}? ")))
    tot_gols += gols[i]
jogador['Gols'] = gols.copy()
jogador['Total_Gols'] = tot_gols

print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'{k} -> {v}')
print('=-'*30)

print(f"O jogador {jogador['Nome']} jogou {qtd_partidas} partidas")
for k, i in enumerate(jogador['Gols']):
    print(f"   => Na partida {k+1} ele fez {i} gols")
    k += 1
print("Foi um total de ", jogador['Total_Gols'], "gols")
print('=-'*30)
