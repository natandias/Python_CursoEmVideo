maiores_de_18 = 0
homens = 0
mulheres_menos_de_20 = 0

while 1:
    print("="*10, "CADASTRO DE PESSOA", "="*10)

    idade = int(input("Idade: "))
    if idade >= 18:
        maiores_de_18 += 1

    sexo = str(input("Sexo[F/M]: ")).strip().upper()
    while sexo not in "FM":
        sexo = str(input("Sexo[F/M]: ")).strip().upper()
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

    continuar = str(input("Continuar? [S/N]?")).strip().upper()
    while continuar not in "SN":
        continuar = str(input("Continuar? [S/N]?")).strip().upper()

    if continuar == 'N':
        break

print("\n")
print("Quantidade de pessoas com mais de 18 anos:", maiores_de_18)
print("Quantidade de homens:", homens)
print("Quantidade de mulheres com menos de 20 anos:", mulheres_menos_de_20)
print("\n")
