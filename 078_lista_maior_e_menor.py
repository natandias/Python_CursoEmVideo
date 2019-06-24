lista = []

print("==Você deve digitar 5 valores==")
for i in range(0, 5):
    lista.append(int(input(f"Digite o valor para a posição {i}: ")))
print("\nForam digitados os seguintes valores:", end=' ')
for i in lista:
    print(i, end='  ')

maior = max(lista)
menor = min(lista)
print(f"\nO maior valor digitado foi {maior} e está nas posições: ", end=' ')
for ps, elem in enumerate(lista):
    if elem == maior:
        print(ps, end='... ')

print(f"\nO menor valor digitado foi {menor} e está nas posições:", end='  ')
for ps, elem in enumerate(lista):
    if elem == menor:
        print(ps, end='... ')
print("\n")
