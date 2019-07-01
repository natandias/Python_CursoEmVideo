def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um numero.
    :param num: O numero a ser calculado o fatorial.
    :param show: opcional, mostra ou não a operação realizada
    :return: resultado da operação
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show == True:
            print(f'{c}', end=' ')
            if c-1 != 0:
                print('* ', end='')
            else:
                print('=', end=' ')
    print(fat)


print()
print("--"*23)
num = int(input("Numero a se obter fatorial: "))
show = str(input("Deseja mostrar a operação detalhada[S/N]? "))
while show not in 'SsNn':
    print()
    print('Responda somente S ou N')
    show = str(input("Deseja mostrar a operação detalhada[S/N]? "))
if show in 'Ss':
    show = True

print()
print(f'Fatorial de {num}')
print('--'*15)
fatorial(num, show)
print()
