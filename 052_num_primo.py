num = int(input("Digite o numero que deseja saber se é primo: "))

nao_primo = 0
for i in range(1, num+1):
    if 1 < i < num:
        if num%i==0:
            nao_primo += 1

if num==1:
    print (f"{num} não é primo")
elif nao_primo > 0:
    print (f"{num} não é primo")
else:
    print (f"{num} é primo")