from datetime import date

dia_nasc = int(input("Qual o dia de nascimento do atleta? "))
mes_nasc = int(input("Qual o mês de nascimento do atleta? (em numero): "))
ano_nasc = int(input("Qual o ano de nascimento do atleta? "))

ano_atual = int(date.today().year)
mes_atual = int(date.today().month)
dia_hoje = int(date.today().day)

idade = ano_atual-ano_nasc
if mes_atual < mes_nasc:
    idade = idade - 1
if mes_atual == mes_nasc and dia_hoje < dia_nasc:
    idade = idade - 1

if idade <= 9:
    print(f"O atleta tem {idade} anos e está na categoria MIRIM")
elif idade <= 14:
    print(f"O atleta tem {idade} anos e está na categoria INFANTIL")
elif idade <= 19:
    print(f"O atleta tem {idade} anos e está na categoria JUNIOR")
elif idade <= 25:
    print(f"O atleta tem {idade} anos e está na categoria SÊNIOR")
else:
    print(f"O atleta tem {idade} anos e está na categoria MASTER")
