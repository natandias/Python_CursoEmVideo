distancia = float(input("Qual a distância total da viagem em km:  "))

while distancia==0 or distancia<0:
    print ("\nA distância deve ser maior do que 0") 
    distancia = float(input("Qual a distância total da viagem em km:  "))

if distancia<200: print (f"\nPreço da passagem: R${0.50*distancia:.2f}")
else: print (f"\nPreço da passagem: R${0.45*distancia:.2f}")