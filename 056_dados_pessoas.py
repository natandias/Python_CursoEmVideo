nome = []
idade = []
sexo = []
soma = 0
maior = 0
mulh_menos_vinte = 0
nome_mais_velho = ''


for i in range (1, 5):
    print ("-"*5, i, "ª PESSOA","-"*5)
    nome.append(str(input("Qual o nome da pessoa: ").strip()))
    idade.append(int(input("Qual a idade da pessoa: ")))
    sexo.append(str(input("Qual o sexo da pessoa [m ou f]:  ").lower().strip()))
    print ("\n")
 
    soma += idade[i-1]

    if idade[i-1] > maior and sexo[i-1] == 'm': 
        maior = idade[i-1]
        nome_mais_velho = nome[i-1]
        idade_m_velho = idade[i-1]
    
    if idade[i-1] < 20 and sexo[i-1] == 'f':
        mulh_menos_vinte += 1

if mulh_menos_vinte == 1:
    s = ''
else:
    s = 'es'

print ("A média de idade do grupo é:", soma/len(idade),"anos")

if nome_mais_velho != '':
    print ("O homem mais velho é:", nome_mais_velho, "com", idade_m_velho,"anos")
else:
    print("Não foi cadastrado nenhum homem")
    
print(f"Há no grupo {mulh_menos_vinte} mulher{s} com menos de 20 anos")
print ("\n")

    
