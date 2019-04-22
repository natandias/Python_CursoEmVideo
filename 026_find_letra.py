frase = str(input("Digite uma frase qualquer:  ")).strip()

frase = frase.lower()
print (f"A letra 'a' aparece {frase.count('a')} vezes na frase")
print (f"A letra 'a' aparece pela primeira vez na posição {frase.find('a')+1}")
print (f"A letra 'a' aparece pela última vez na posição { frase.rfind('a')+1 }")

