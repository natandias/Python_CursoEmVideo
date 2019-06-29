from time import sleep


def contagem(ini, fim, passo):
    print()
    print('=-'*20)
    if ini < fim:
        fim += 1
        if passo == 0:
            passo = 1
        if passo < 0:
            passo = passo * -1
        print(f'Contagem de {ini} a {fim-1}, de {passo} em {passo}')
    elif ini > fim:
        fim -= 1
        if passo == 0:
            passo = -1
        elif passo > 0:
            passo = passo * -1
        print(f'Contagem de {ini} a {fim+1}, de {passo} em {passo}')
    for i in range(ini, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.1)
    print('END')
    print('=-'*20)


# MAIN
contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(
    int(input("Início: ")),
    int(input("Fim: ")),
    int(input("Passo: "))
)
