extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

continuar = 'S'

while continuar == 'S':
    num = int(input("Digite um numero[0 a 20]: "))
    while(num < 0) or (num > 20):
        num = int(input("Digite um numero[0 a 20]: "))
    print("Numero por extenso:", extenso[num])
    continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
