import math

cateto_op = float(input("Digite o comprimento do cateto oposto: "))
cateto_adj = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = cateto_adj**2 + cateto_op**2
hipotenusa = math.sqrt(hipotenusa)
print ("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))
print (f"A hipotenusa vai medir: {math.hypot(cateto_op, cateto_adj):.2f}")