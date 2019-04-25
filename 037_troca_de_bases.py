num = int(input("Digite o numero a ser convertido: "))
print("Digite 2 para binário, 8 para octal ou 16 para hexadecimal")
base = int(input("Base a qual deseja converter:  "))
numero = num #armazena o numero para ser utilizado no print

i = 0
resto = []
if base == 2:
    while (num >= 2):
        resto.append(num % 2)
        num = num // 2
        i += 1

    print(f"O numero {numero} em binário é representado por: ", end='')
    print(num, end='')
    k = len(resto)
    while (k != 0):
        print(resto[k-1], end='')
        k = k-1
    print("\n")

i = 0
resto = []
if base == 8:
    while (num >= 8):
        resto.append(num % 8)
        num = num // 8
        i += 1
 
    print(f"O numero {numero} em octal é representado por: ", end='')
    print(num, end='')
    k = len(resto)
    while (k != 0):
        print(resto[k-1], end='')
        k = k-1
    print("\n")

i = 0
resto = []
if base == 16:
    while (num >= 16):
        resto.append(num % 16)
        num = num // 16
        i += 1
    
    print(f"O numero {numero} em hexadecimal é representado por: ", end='')
    print(num, end='')
    k = len(resto)
    while (k != 0):
        print(resto[k-1], end='')
        k = k-1
    print("\n")