from random import randint
from time import sleep
from operator import itemgetter

player = dict()
todos = []
maior = 0   

print("\nJogando dados...........")
sleep(0.3)
for j in range(0, 4):
    dado = randint(1, 6)
    player['id'] = j
    player['jogada'] = dado
    todos.append(player.copy())

print('Valores sorteados:')
for i in todos:
    print(f"\tO jogador {i['id']+1} tirou {i['jogada']}")
    sleep(0.7)

k = 1
print("\n")
print(" "*5,"=-"*9,"Ranking Geral", "=-"*9)
ordenado = sorted(todos, key=itemgetter('jogada'), reverse=True)
for p, i in enumerate(ordenado):
    print(" "*5,"||", end='')
    print(f"\t{k}º Lugar:", end=' ')
    print(f"Jogador {ordenado[p]['id']+1} com {ordenado[p]['jogada']} pontos", end=' '*7)
    print("||")
    k += 1
    sleep(0.7)
print(" "*5,"=-"*25)
