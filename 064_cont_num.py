i = 1
num = int(input("Digite um número: "))
while num != 999:
    num = int(input("Digite outro número: "))
    if num != 999:
        i += 1

print (f"\nForam digitados {i} números\n")