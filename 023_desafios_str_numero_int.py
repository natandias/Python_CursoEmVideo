import math

num = int(input("Digite um numero inteiro entre 0 e 9999: "))

while (num>9999 or num<0):
    print ("Esse numero é maior que 9999 ou menor que 0")
    num = int(input("Digite um numero entre 0 e 9999: "))

milhares = math.trunc (num/1000)
centenas = num%1000
dezenas = centenas%100
unidades = dezenas%10

print (f"milhares: {milhares}")
print (f"centenas: {math.trunc(centenas*0.01)}")
print (f"dezenas: {math.trunc(dezenas*0.1)}")
print (f"unidades: {unidades}")

