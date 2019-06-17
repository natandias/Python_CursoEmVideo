while 1:
    num = int(input("Digite o numero que deseja obter a tabuada (0 para sair): "))

    if(num == 0): 
        print("See you soon")
        break

    while(num < 0):
        num = int(input("Digite um numero maior que 0: "))

    print(f"\n================TABUADA DE {num}================\n")
    for i in range(1, 11):
        print("{} {} x {} = {}".format(' '*13, num, i, num*i))
  
    print('='*63)
