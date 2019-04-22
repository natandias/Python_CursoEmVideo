import math

num = int(input("Digite um numero entre 0 a 9999: "))

while (num>9999 or num<0):
    print ("Esse numero é maior que 9999 ou menor que 0")
    num = int(input("Digite um numero inteiro entre 0 e 9999: "))
    
unidade = num // 1  % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhares = num // 1000 % 10
 
print (f"unidade: {unidade} ")
print (f"dezena: {dezena} ")
print (f"centena: {centena} ")
print (f"milhares: {milhares} ")


