def leiaInt(scan):
    temp = input("Digite um numero: ")
    while True:
        if temp.isnumeric() is False:       
            print('\033[31m'+'Isso não é um numero inteiro'+'\033[0;0m')
            temp = input('Digite um numero: ')
        elif temp.isnumeric() is True:
            int(temp)
            return temp


print('---'*10)
num = leiaInt('Digite um numero: ')
print(f"O número digitado foi {num}")
print()
