from time import sleep
from random import random
jogo_unico = []
jogos = list()

print('=_'*10,'GERADOR DE NÚMEROS PARA MEGASENA', '_='*10)
qtd_jogos = int(input("Quantos jogos irá fazer? "))

for k in range(0, qtd_jogos):
    jogo_unico.clear()
    for i in range(0, 6):
        num = round(random()*60)
        while num in jogo_unico:
            num = round(random()*60)
        jogo_unico.append(num)
    jogo_unico.sort()
    jogos.append(jogo_unico[:])

print("\nEsses são seus números: ")
for i in range(0, len(jogos)):
    sleep(0.4)
    print(f"Jogo {i+1}: {jogos[i]}")

print('\n','-='*8, "BOA SORTE, SE GANHAR NÃO ESQUEÇA DE NÓS", '-='*8)
