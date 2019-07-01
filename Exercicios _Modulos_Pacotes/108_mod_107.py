from utilidades.moeda import moeda

print()
ini = float(input('Digite o valor: R$ '))
print(f'A metade de {ini} é {moeda.moeda(moeda.metade(ini))}')
print(f'O dobro de {ini} é {moeda.moeda(moeda.dobro(ini))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(ini, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(ini, 13))}')
print()