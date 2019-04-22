cidade = (str(input("Digite o nome da cidade:  ")).strip().lower())
if(cidade.find("santo")==0):
    print ("O nome da cidade começa com Santo")

nome = (str(input("Digite o nome da pessoa: ")).strip().lower())
nome = nome.split()

if ('silva' in nome):
    print ("O nome possui Silva")

