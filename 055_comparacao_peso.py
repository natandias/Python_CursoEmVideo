maior = 0
menor = 0
for i in range (1, 6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    if i == 1:  
        maior = peso 
        menor = peso
    else: 
        if peso > maior: maior = peso
        if peso < menor: menor = peso

print("O maior peso é:", maior, 'kg')
print("O menor peso é:", menor, 'kg', '\n')

'''ou de forma mais eficiente:
pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print('O maior peso é {}Kg' .format(max(pesos)))
print('O menor peso é {}Kg' .format(min(pesos)))'''