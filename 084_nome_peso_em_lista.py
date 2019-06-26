pessoas = list()
individuo = list()
maior = menor = 0
mais_pesadas = []
mais_leves = []

while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    pessoas.append(individuo[:])
    individuo.clear()

    continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if continuar == 'N':
        break

for c, pessoa in enumerate(pessoas):
    if c == 0:
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maior:
        mais_pesadas.append(pessoa[0])
    if pessoa[1] == menor:
        mais_leves.append(pessoa[0])

print(f"\nForam cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi {maior} kg. Peso de:", end=' ')
for i in mais_pesadas:
    print(i, end=' - ')
print(f"\nO menor peso foi {menor} kg. Peso de:", end=' ')
for i in mais_leves:
    print(i, end=' - ')
print("\n")