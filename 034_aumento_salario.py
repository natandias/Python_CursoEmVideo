salario = float(input("Digite o salário do funcionário: "))

if salario>1250: aumentado = salario*1.10
else: aumentado = salario*1.15

print ("O salário do funcionário com aumento é igual a: R$ {:.2f}".format(aumentado))