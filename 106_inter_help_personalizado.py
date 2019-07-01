while True:
    print('\n')
    print('\033[45m'+'=='*29)
    print(' '*16, 'AJUDA DO PYTHON', ' '*25)
    print('=='*29+'\033[0;0m')
    print('Digite uma função ou biblioteca para obter ajuda sobre: ')
    com = str(input(' '*15)).strip().lower()
    if com == 'fim':
        print('\033[42m'+'=='*29)
        print(' '*16, 'ATÉ LOGO', ' '*32)
        print('=='*29+'\033[0;0m')
        break
    print('\n')
    help(com)