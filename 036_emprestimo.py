valor_casa = float(input("Qual o valor da casa? \n R$ "))
salario = float(input("Qual o salário do comprador? \n R$ "))
tempo = int(input("Em quantos anos ele irá pagar? \n "))

tempo = tempo*12; #transforma os anos em meses
valor_parcela = valor_casa/tempo; 

while valor_casa/tempo > salario*0.30:
    tempo += 1

if valor_parcela <= salario*0.30:
    print ("Empréstimo concedido")
    print (f"Você deverá pagar {tempo} parcelas de R${valor_parcela:.2f}\n")
else: 
    print ("Infelizmente, não podemos lhe conceder o empréstimo nesse momento")
    print (f"Seriam necessárias {tempo} parcelas de {valor_parcela:.2f}, o que excede 30% do seu salário \n")
 
