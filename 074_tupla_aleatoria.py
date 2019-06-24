from random import random

tupla = (round(random()*100), round(random()*100), round(random()*100),
         round(random()*100), round(random()*100))

print("\nValores sorteados:", tupla)

ordered = sorted(tupla)
print("\nMenor numero:", ordered[0])  # ou print (min(tupla))
print("Maior numero:", ordered[-1])  # ou print (max(tupla))
print("\n")
