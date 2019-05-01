num = int(input("Digite um numero: "))
razao = int(input("Digite a razão da PA: "))

print (num, end = ' ')
for i in range (1, 10):
    print (num+razao, end=' ') 
    num += razao