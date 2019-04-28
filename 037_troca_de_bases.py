num = int(input("Digite o numero a ser convertido: "))

print('''Escolha a base para qual deseja converter: 
[   2  ] Binário
[   8  ] Octal
[  16  ] Hexadecimal
''')
base = int(input("Base a qual deseja converter:  "))

while base != 2 and base != 8 and base != 16:
        print("\nVocê escolheu uma opção inválida!!!")
        base = int(input("Escolha entre base 2, base 8 ou base 16: "))


numero = num  # armazena o numero para ser utilizado no print

i = 0
resto = []
if base == 2:
    while (num >= 2):
        resto.append(num % 2)
        num = num // 2
        i += 1

    print(f"O numero {numero} em binário é representado por: ", end='')
    binario = str(num)
    k = len(resto)
    while (k != 0):
        binario += str(resto[k-1])
        k = k-1

    print(binario)
    print("\n")

i = 0
resto = []
if base == 8:
    while (num >= 8):
        resto.append(num % 8)
        num = num // 8
        i += 1

    print(f"O numero {numero} em octal é representado por: ", end='')
    octal = str(num)
    k = len(resto)
    while (k != 0):
        octal += str(resto[k-1])
        k = k-1

    print(octal)
    print("\n")

i = 0
resto = []
if base == 16:
    while (num >= 16):
        resto.append(num % 16)
        num = num // 16
        i += 1

    print(f"O numero {numero} em hexadecimal é representado por: ", end='')
    hexa = str(num)
    k = len(resto)
    while (k != 0):
        hexa += str(resto[k-1])
        k = k-1

    hexa = hexa.replace('10', 'A')
    hexa = hexa.replace('11', 'B')
    hexa = hexa.replace('12', 'C')
    hexa = hexa.replace('13', 'D')
    hexa = hexa.replace('14', 'E')
    hexa = hexa.replace('15', 'F')

    print(hexa)
    print("\n")
