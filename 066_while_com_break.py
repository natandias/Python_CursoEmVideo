soma = 0
cont = 0

while 1:
    num = int(input("Digite numero a ser somado (Digite 999 para parar): "))
    if num == 999: 
        break
    soma += num
    cont += 1

print(f"\nForam digitados {cont} numeros")
print(f"O total da soma dos numeros digitados é {soma}\n")