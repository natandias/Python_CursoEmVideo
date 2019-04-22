speed = float(input("Qual a velocidade do carro em km/h: "))

if speed>80:
    excesso = speed - 80
    print (f"Você foi multado em: R${7*excesso:.2f} por estar a {excesso}km/h a mais que o limite de 80km/h que é o permitido na via\n")
else: 
    if speed<80 and speed>40: print ("Parabéns. Você é um motorista exemplar !!\n") 
    
    if speed<40: 
        abaixo = 80-speed 
        print (f"Sua tartaruga. Você foi multado em R${7*abaixo:.2f} por estar a {abaixo}km/h abaixo do limite\n")