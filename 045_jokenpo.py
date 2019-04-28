import random

print ("===============BEM AO VINDO AO JOKENPÔ================")
print('''
[ 1 ] JOGAR
[ 2 ] REGRAS
[ 3 ] SAIR
''')
opcao = int(input(""))
if opcao == 3:
    exit (1)
if opcao == 2:
    print ('''[ Pedra ganha da tesoura (amassando-a ou quebrando-a) ]
[ Tesoura ganha do papel (cortando-o) ]
[ Papel ganha da pedra (embrulhando-a ]\n''')
else: 
    jogada = 'pedra', 'papel', 'tesoura'
    sair = 'y'
    v_p1 = 0
    v_com = 0

    print("Digite SAIR a qualquer momento")
    while (sair != 'sair'):
        p1 = str(input("Qual sua jogada: Pedra, Papel ou Tesoura: ")).strip().lower()  
         
        if p1 == 'sair':
            break

        while (p1 != 'pedra' and p1 != 'papel' and p1 != 'tesoura'):
            print ("Jogada inválida!!! Escolha pedra, papel ou tesoura")
            p1 = str(input("Qual sua jogada: Pedra, Papel ou Tesoura: ")).strip().lower() 

        com = random.choice(jogada)
        print ("=+"*20)
        print (f"Você jogou {p1}")
        print(f"O computador jogou {com}")

        if p1 == 'pedra':
            if com == 'pedra':
                print('Empate')
            if com == 'papel':
                print(':( Você perdeu essa mas pode tentar de novo ):')
                v_com += 1
            if com == 'tesoura':
                print('Você ganhou !!!')
                v_p1 += 1
            #print("\n")

        elif p1 == 'papel':
            if com == 'papel':
                print('Empate')
            if com == 'tesoura':
                print(':( Você perdeu essa mas pode tentar de novo ):')
                v_com += 1
            if com == 'pedra':
                print('Você ganhou !!!')
                v_p1 += 1
            #print("\n")

        elif p1 == 'tesoura':
            if com == 'tesoura':
                print('Empate')
            if com == 'pedra':
                print(':( Você perdeu essa mas pode tentar de novo ):')
                v_com += 1
            if com == 'papel':
                print('Você ganhou !!!')
                v_p1 += 1

        print ("=+"*20)
        print("\n")

        
    print (f"Você ganhou {v_p1} vezes e o computador ganhou {v_com} vezes\n")