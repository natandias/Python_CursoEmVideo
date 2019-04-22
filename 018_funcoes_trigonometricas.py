import math

angulo = float(input("Digite o angulo em graus: "))
angulo = math.radians (angulo)
print (f"O seno do angulo é: {math.sin(angulo):.5f}")
print (f"O cosseno do angulo é: {math.cos(angulo):.5f}")
print (f"A tangente do angulo é: {math.tan(angulo):.5f}")