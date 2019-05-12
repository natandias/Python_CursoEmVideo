sn = 'S'
cont = 0
soma = 0

while sn == 'S':
    num = int(input("Digite um numero: "))
    
    soma += num
    if cont == 0: maior = num; menor = num;
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    cont += 1

    sn = str(input("Deseja inserir outro número [S/N]: ")).strip().upper() 
    while sn != 'S' and sn != 'N':
        sn = str(input("Digite S se deseja continuar ou N se deseja parar: ")).strip().upper() 

print ("\n")
print (f"A média entre esses números é: {soma/cont}")
print(f"O menor número desse grupo é {menor}")
print(f"O maior número desse grupo é {maior}")
print ("\n")