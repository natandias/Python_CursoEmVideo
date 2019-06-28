aluno = {}
classe = []

while True:
    print()
    aluno['nome'] = str(input("Nome do aluno: ")).strip()
    aluno['media'] = float(input("Média do aluno: "))
    if aluno['media'] >= 7.0:
        aluno['situacao'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'Em Recuperação'
    else:
        aluno['situacao'] = 'Reprovado'
    classe.append(aluno.copy())

    add = str(input("Adicionar mais alunos[S/N]: ")).strip().upper()
    while add not in 'SN':
        add = str(input("Adicionar mais alunos[S/N]: ")).strip().upper()
    if add == 'N':
        break

print('\nSituação Acadêmica:')
for estudante in classe:
    print(f"{estudante['nome']} -> {estudante['situacao']}")
