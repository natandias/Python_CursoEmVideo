from random import randint

num = randint(0,11)
cont = 0

print ('''O computador escolheu um número aleatório que está entre 0 e 5.
Tente adivinhar qual é o número.
''')

chute = int(input("Qual número você acha que é: "))

while (chute != num):
    chute = int(input("ERROU.\nTente outro:  "))
    cont += 1 
    
if chute==num: print (f"Você acertou com {cont} tentativas\n" )

  
