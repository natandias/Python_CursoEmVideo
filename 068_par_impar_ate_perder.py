from random import randint


par_impar = ["IMPAR", "PAR"]
wins = 0

while 1:
    jogador = str(input("PAR OU IMPAR: ")).upper().strip()

    while jogador not in par_impar:
        jogador = str(input("Escolha entre PAR OU IMPAR: ")).upper().strip()

    num_jogador = int(input("Qual número você joga:"))

    num_maquina = randint(0, 10)
    soma = num_jogador + num_maquina

    if (jogador == "PAR" and (soma) % 2 == 0):
        wins += 1
        print("="*60, "\n")
        print(f"Você pediu {jogador} e jogou o numero {num_jogador}, a máquina jogou {num_maquina}")
        print(f"{num_jogador} + {num_maquina} = {soma}")
        print("Você ganhou essa!!\n")
        print("="*60)

    elif (jogador == "IMPAR" and (soma) % 2 != 0):
        wins += 1
        print("="*60, "\n")
        print(f"Você pediu {jogador} e jogou o numero {num_jogador}, a maquina jogou {num_maquina}")
        print(f"{num_jogador} + {num_maquina} = {soma}")
        print("Você ganhou essa!!\n")
        print("="*60)

    else:
        print("Você perdeu !!")
        print("\n")
        print(f"Você pediu {jogador} e jogou o numero {num_jogador}, a maquina jogou {num_maquina}")
        print(f"{num_jogador} + {num_maquina} = {soma}")
        print("\n", "*"*20, "GAME OVER", "*"*20)
        if wins != 0:
            print(" "*8, f"Você ganhou {wins} partidas consecutivas")
            print("\n")
        break
