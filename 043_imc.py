peso = float(input("Digite o seu peso: "))
altura = int(input("Digite a sua altura em cm: "))

imc = peso /((altura/100)**2)

print (f"Seu imc é {imc:.2f}")
if imc<18.5: 
    print("Abaixo do peso")
elif imc < 25:
    print ("Peso normal")
elif imc <30:
    print ("Sobrepeso")
elif imc <40:
    print ("Obesidade")
elif imc >40:
    print ("Obesidade mórbida")