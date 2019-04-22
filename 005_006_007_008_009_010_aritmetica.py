num = int(input("Digite um numero inteiro:  "))
num2 = int(input("Digite outro numero:  "))

print (f"Antecessor de {num}: {num-1}")
print (f"Sucessor de {num}: {num+1}")

print(f"Dobro de {num} = {num*2}")
print(f"Triplo de {num} = {num*3}")

print(f"Raiz quadrada de {num} = {num**(1/2):.5f}")

print(f"A media entre {num} e {num2} é {(num+num2)/2}")

print(f"{num} metros = {num/1000}km = {num/100}hm = {num/10}dam = {num*10}dm = {num*100}cm = {num*1000}mm")

print ("{:=^30}".format("Tabuada"))
for i in range(1, 11):
 if i>10: print (f"{num} * {i} =  {num*i}") 
     
    

real = float (input  ("Digite quanto dinheiro em R$ você possui: "))
print (f"Você pode comprar {real/3.27:.2f} doláres")