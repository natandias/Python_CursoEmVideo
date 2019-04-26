nota = 0 
cont = 0
for i in range (2):
    nota += int(input("Digite a nota do aluno: "))
    cont = cont+1

media = nota/cont
print ("A média do aluno foi: ", media)

if media < 5.0: 
    print("Infelizmente, o aluno foi reprovado")
elif media > 5.0 and media < 6.9:
    print ("O aluno está de recuperação")
else:
    print ("O aluno foi aprovado")

print ("\n")