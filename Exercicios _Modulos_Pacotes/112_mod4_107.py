from utilidades import moeda, dado

print()
ini = dado.leiaDinheiro(input('Digite o valor: R$ '))
moeda.resumo(ini, 80, 35)
