numeros = [[], []]

for i in range(0, 7):
    num = (int(input('Digite um numero: ')))
    if num % 2 == 0:
        numeros[0].append(num)
    else: 
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print("\nOs valores pares digitados foram:", end=' ')
for i in numeros[0]:
    print(f"[{i}]", end=' ')
print('\nOs valores ímpares digitados foram:', end=' ')
for i in numeros[1]:
    print(f"[{i}]", end=' ')
print("\n") 