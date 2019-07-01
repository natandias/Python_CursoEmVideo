from utilidades.moeda import moeda

print()
ini = float(input('Digite o valor: R$ '))
print(f'A metade de {moeda.moeda(ini)} é {moeda.metade(ini, True)}')
print(f'O dobro de {moeda.moeda(ini)} é {moeda.dobro(ini, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(ini, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(ini, 13, True)}')
print()