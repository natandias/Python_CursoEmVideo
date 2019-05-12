sexo = str(input("Digite o seu sexo [M/F]: " )).upper().strip()

while (sexo != 'M' and sexo != 'F'):
    print("Você digitou uma entrada inválida !!!")
    sexo = str(input("Digite o seu sexo [M/F]: " )).upper().strip()