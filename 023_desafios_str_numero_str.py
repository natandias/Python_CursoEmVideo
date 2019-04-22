num = int(input("Digite um numero inteiro entre 0 e 9999: "))

while (num>9999 or num<0):
    print ("Esse numero é maior que 9999 ou menor que 0")
    num = int(input("Digite um numero inteiro entre 0 e 9999: "))

num = str(num)

if (len(num)==4):
    print (f"unidade = {num[3]}")
    print (f"dezena = {num[2]}")
    print (f"centena = {num[1]}")
    print (f"milhar = {num[0]}")

if (len(num)==3):
    print (f"unidade = {num[2]}")
    print (f"dezena = {num[1]}")
    print (f"centena = {num[0]}")
    print ("milhar = 0")

if (len(num)==2):
    print (f"unidade = {num[1]}")
    print (f"dezena = {num[0]}")
    print ("centena = 0")
    print ("milhar = 0")

if (len(num)==1):
    print (f"unidade = {num[0]}")
    print ("dezena = 0")
    print ("centena = 0")
    print ("milhar = 0")


