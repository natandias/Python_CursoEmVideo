aluno = []
all_alunos = []
notas_aluno = list()

while True:
    print()
    aluno.append(str(input('Digite nome do aluno: ')).strip())
    print("Use ponto para decimais[Ex: 9.6]")
    notas_aluno.append(float(input('Digite primeira nota: ')))
    notas_aluno.append(float(input('Digite segunda nota: ')))

    aluno.append(notas_aluno[:])
    all_alunos.append(aluno[:])
    notas_aluno.clear()
    aluno.clear()

    continuar = str(input('Deseja adicionar outro aluno[S/N]? ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar outro aluno[S/N]? ')).strip().upper()
    if continuar == 'N':
        break

print("\n")
print("-"*48)
print('|-|'*5, "NOTAS DA CLASSE", '|-|'*5)
print("-"*48)
print(f'{"No.":<4} {"Nome":<15} {"Media":>8}')
for i in range(0, len(all_alunos)):
        print(f"{i}.", " ", all_alunos[i][0], end='')
        print(f"{((all_alunos[i][1][0]+all_alunos[i][1][1])/2):>8}")
print("\nDeseja ver notas detalhadas do aluno? ")

while True:
    cod_aluno = int(input("Código do aluno desejado: [-1 para cancelar]: "))
    if cod_aluno == -1:
        break
    while cod_aluno > len(all_alunos)-1:
        cod_aluno = int(input("Código inválido!! Digite um código existente: "))
    print("Aluno:", all_alunos[cod_aluno][0], end=' -> ')
    print(f"1ª nota: {all_alunos[cod_aluno][1][0]}, 2ª nota: {all_alunos[cod_aluno][1][1]}")
    print()
