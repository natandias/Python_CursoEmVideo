nome = (str(input("Digite seu nome completo: "))).strip()
print ("Nome em maiúsculo: ", nome.upper())
print ("Nome em minúsculo: {}".format(nome.lower()))
#separa o nome em razão do espaço entre as palavras, logo após junta sem espaços e calcula o length
print (f'Tamanho do nome, sem contar espaços: {len("".join(nome.split()))} letras')  

#a lista p recebe os nomes separados com p[0] sendo o primeiro nome
p = nome.split()
print(f"Seu primeiro nome é: {p[0]} e ele possui {len(p[0])} letras \n" ) 