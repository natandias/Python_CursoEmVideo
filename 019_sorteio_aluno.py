import random

i = 0
alunos = []
for i in  range(1,5):
    alunos.append (str(input("Digite o nome do aluno {}: ".format(i))))

selected = random.choice(alunos)
print (f"O escolhido foi {selected}")
