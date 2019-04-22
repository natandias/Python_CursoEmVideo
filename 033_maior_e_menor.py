num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1>num2:
    maior = num1
    menor = num2
    if num3>maior:
        maior = num3
else: 
    maior = num2
    menor = num1
    if num3>maior:
        maior = num3

print (f"O maior é: {maior}")
print (f"O menor é: {menor}")