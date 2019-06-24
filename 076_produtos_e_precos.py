lista = ('Leite', 2.50, 'Manteiga', 15.00, 'Ovo', 8.00, 'Suco de Uva', 3.00,
         'Arroz', 11.00, 'Feijão', 10.00, 'Oleo', 2.50, 'Biscoito', 2.00)

print("-"*40)
print(f'{"LISTA DE PREÇOS":^40}')
print("-"*40)

i = 0
for k in range(0, len(lista)-8):
    print(f"{lista[i]}", '.'*(30-len(lista[i])), f"R$ {lista[i+1]:>6.2f}")
    i += 2
print("\n")
