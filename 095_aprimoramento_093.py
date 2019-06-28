jogador = {}
gols = []
todos_jogadores = []

while True:
    gols.clear()
    jogador.clear()
    tot_gols = 0
    print()
    jogador['Nome'] = str(input("Nome do jogador: ")).strip()
    jogador['qtd_partidas'] = int(input("Ele jogou quantas partidas? "))
    for i in range(0, jogador['qtd_partidas']):
        gols.append(int(input(f"Quantos gols fez na partida {i+1}? ")))
        tot_gols += gols[i]
    jogador['Gols'] = gols.copy()
    jogador['Total_Gols'] = tot_gols
    todos_jogadores.append(jogador.copy())

    add = str(input("Cadastrar mais jogadores[S/N]? ")).upper().strip()
    while add not in 'SN':
        add = str(input("Cadastrar mais jogadores[S/N]? ")).upper().strip()
    if add == 'N':
        break

print()
print("=-"*30)
for jogador in todos_jogadores:
    print(f"{jogador['Nome']} fez {jogador['Total_Gols']} gols em {jogador['qtd_partidas']} partidas")
print('=-'*30)

while True:
    print()
    print("Deseja detalhes sobre algum jogador?")
    print("Digite SAIR a qualquer momento")
    info = str(input("Nome do jogador: ")).upper().strip()
    if info == 'SAIR':
        break
    find = 0
    for jogador in todos_jogadores:
        if jogador['Nome'].strip().upper() == info:
                k = 1
                for i in jogador['Gols']:
                    print(f" => Na {k}ª partida, ele fez {i} gols")
                    k += 1
                print("\033[32m"+jogador['Nome']+"\033[0;0m"+f" fez um total de {jogador['Total_Gols']} gols")
                find = 1
    if find == 0: 
        print('\033[31m'+"Jogador não encontrado"+'\033[0;0m')
print('=-'*50)
