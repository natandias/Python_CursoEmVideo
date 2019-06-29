def maior(* num):
    maior = 0
    cont = 0
    print('=-='*15)
    print('||', 'Sequência informada: ', end=' ')
    for i in num:
        cont += 1
        print(i, end='  ')
        if i > maior:
            maior = i
    if cont == 0: print('Nada informado', end=' ')
    print()
    print('||', f'Foram informados {cont} valores ao todo', ' '*4)
    print('||', f"O maior valor dessa sequencia é: {maior}", ' '*4)
    print('=-='*15)
    print()

print('=-='*15)
print('||', ' '*13, "BEM VINDO!!!", ' '*12, '|| ')
print('=-='*15)
print()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
