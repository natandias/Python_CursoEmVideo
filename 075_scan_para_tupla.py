nums = []
pares = []

''' pode - se usar
    num = (int(input('Digite um num: ')), int(input('Digite um num: '))) '''
 
for i in range(0, 4):
    nums.append(int(input("Digite um valor: ")))

tupla = (nums[0], nums[1], nums[2], nums[3])

print("\n")
print("O numero 9 apareceu:", tupla.count(9), "vez(es)")
if 3 in tupla:
    print("O valor 3 está na posição:", tupla.index(3)+1)
else:
    print("O valor 3 não está na tupla")

for i in tupla:
    if (i % 2) == 0:
        pares.append(i)

print("Os numeros pares dessa tupla são: ", end=' ')
for i in pares:
    print(i, end=" "*3)
print("\n")
