import random

jogada = 'pedra', 'papel', 'tesoura'
sair = 'y'
v_p1 = 0
v_com = 0

print("Digite SAIR a qualquer momento")
while (sair != 'SAIR'):
    p1 = str(input("Qual sua jogada: Pedra, Papel ou Tesoura: ")).strip().lower()  
    
  
    com = random.choice(jogada)

    print(f"O computador jogou {com}")

    if p1 == 'sair':
        break

    elif p1 == 'pedra':
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
    print("\n")

print (f"Você ganhou {v_p1} vezes e o computador ganhou {v_com} vezes\n")