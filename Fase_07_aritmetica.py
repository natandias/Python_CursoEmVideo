#pode ser 'casted' pra int, float, str ou bool
num1 =int( input("Digite valor: "))
num2 = int(input("Outro: "))

#métodos
#mais recente
print  (f"A soma entre {num1} e {num2} vale {num1+num2}")
print ("A soma entre", num1, "e", num2, "vale", num1+num2)
#usado antes do python 3.7
print("A soma entre {} e  {} vale {} ".format(num1, num2, num1+num2))

print(f"O produto entre {num1} e {num2} é {num1*num2}")
print(f"O quociente entre {num1} e {num2} é   {num1/num2:.3f} " )
print(f"A potência entre {num1} e {num2} é {num1**num2}")
print(f"A divisão inteira entre {num1} e {num2} é {num1//num2}")

