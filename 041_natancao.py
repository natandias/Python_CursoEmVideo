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


if idade < 9:
    print ("O atleta está na categoria MIRIM")
elif idade > 9 and idade <= 14:
    print ("O atleta está na categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print ("O atleta está na categoria JUNIOR")
elif idade > 19 and idade <= 20:
    print ("O atleta está na categoria SÊNIOR")
else: 
    print ("O atleta está na categoria MASTER")
