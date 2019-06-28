form = dict()  # formulario para cada pessoa
cadastro = list()

while True:
    print()
    form['Nome'] = str(input('Nome da pessoa: '))
    sexo = str(input("Sexo[M/F]: ")).upper().strip()
    while sexo not in 'MF':
        print('\033[31;1m'+'Responda apenas M ou F !!'+'\033[0;0m')
        sexo = str(input("Sexo[M/F]: ")).upper().strip()
    form['Sexo'] = sexo
    form['Idade'] = int(input("Idade: "))
    cadastro.append(form.copy())

    add = str(input("Cadastrar mais pessoas[S/N]? ")).upper().strip()
    while add not in 'SN':
        print('\033[31;1m'+"Responda apenas S ou N !!"+'\033[0;0m')
        add = str(input("Cadastrar mais pessoas[S/N]? ")).upper().strip()
    if add == 'N':
        break
print("\n")

print("=-"*30)
print(f"Foram cadastradas {len(cadastro)} pessoas")
soma_idade = 0
for pessoas in cadastro:
    soma_idade += pessoas['Idade']
media = soma_idade / len(cadastro)
print(f"A média de idade dessas pessoas é {media:.2f} anos")

print("=-"*30)
print("As mulheres cadastradas são: ")
for pessoa in cadastro:
    if pessoa['Sexo'] == 'F':
        print(f"{pessoa['Nome']}, {pessoa['Idade']} anos")

print("=-"*30)
print("Os homens cadastrados são: ")
for pessoa in cadastro:
    if pessoa['Sexo'] == 'M':
        print(f"{pessoa['Nome']}, {pessoa['Idade']} anos")

print("=-"*30)
print("Pessoas com idade acima da média: ")
for pessoa in cadastro:
    if pessoa['Idade'] > media:
        print(f"{pessoa['Nome']}, {pessoa['Sexo']}, {pessoa['Idade']} anos")
