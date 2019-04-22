import random

num_alunos = (int(input("Quantos alunos irão participar: ")))
num_sorteados =  (int(input("Quantos alunos deseja sortear: ")))

i = 0
alunos = []
for i in range (1,num_alunos+1):
    alunos.append (input(f"Digite o nome do aluno {i}: "))

selected = random.sample (alunos, k=num_sorteados)

ordem = 1
print ("\nOrdem de apresentação:")
for k in selected:
    print (f"{ordem}°: {k} \n")
    ordem +=1


