cont1 = 0
cont2 = 0
fechado_aberto = 0  # 0 para fechado, >1 para aberto
invalida = 0

expr = (str(input("Digite uma expressão: ")).strip().lower())
for crt in range(0, len(expr)):
    if expr[crt] == '(':
        cont1 += 1
        fechado_aberto += 1
    elif expr[crt] == ')' and fechado_aberto >= 1:
        cont2 += 1
        fechado_aberto -= 1
    elif expr[crt] == ')' and fechado_aberto == 0:
        invalida = 1
        break

print("\nA expressão digitada foi: ", expr)
if cont1 == cont2 and invalida == 0:
    print("Expressão válida")
elif cont1 > cont2:
    print("Expressão inválida, pois há parênteses sem fechar")
elif invalida == 1:
    print("Expressão inválida, pois fechou-se parênteses a mais")
print('\n')
# ((a+b)*c) (x+y(3+2/3)*z) exemplo de expressao valida
# ((((a+b)*c)+2)/4)) exemplo de expressao invalida
