sn = 'S'
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

print ("O que deseja realizar com esses valores: ")
print ('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')

while sn == 'S':
    choice = int(input("Qual a opção desejada: "))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        choice = int(input("Digite uma opção válida[1 a 5]: "))
    if choice == 1:
        print(f"A soma entre {v1} e {v2} é igual a: {v1+v2}\n")
    elif choice == 2:
        print(f"O produto entre {v1} e {v2} é igual a: {v1*v2} \n")
    elif choice == 3:
        if v1 > v2: print (f"O maior número é: {v1}\n")
        else:  print (f"O maior número é: {v2}\n")
    elif choice == 4:
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
        print ("\nO que deseja realizar com esses valores: ")
        print ('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        ''')

    elif choice == 5:
        print ("Obrigado por utilizar o nosso programa. Volte sempre!!!\n")
        exit(1)
    if choice != 4:
        sn = str(input("Deseja realizar outra operação? [S/N]: ")).strip().upper()
        #controla para que a entrada seja somente 'S' ou 'N'
        while sn != 'S' and sn != 'N':
            sn = str(input("Deseja realizar outra operação? Responda [S ou N]: ")).strip().upper()
       
    