from utilidades.moeda import moeda

print()
ini = float(input('Digite o valor: R$ '))
print(f'A metade de R$ {ini} é R$ {moeda.metade(ini)}')
print(f'O dobro de R$ {ini} é R$ {moeda.dobro(ini)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(ini, 10)}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(ini, 13)}')
print()
