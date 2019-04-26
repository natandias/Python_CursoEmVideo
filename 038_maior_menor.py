num1 = int(input("Digite primeiro numero:  "))
num2 = int(input("Digite segundo numero:  "))

if (num1 > num2): 
    print("O primero numero é maior, pois ", end='')
    print (f"{num1} é maior que {num2}")
elif (num2 > num1): 
    print("O segundo numero é maior, pois ", end='')
    print (f"{num2} é maior que {num1}")
else: print (f"{num1} é igual a {num2}")