from datetime import date, time, datetime

data = datetime.now().strftime('%d/%m/%Y %H:%M')
print("="*10, "POUPANÇA BAMERINDOS", "="*16)
print("BEM VINDO", "-"*20, data)

print("\nCédulas disponíveis: R$50, R$20, R$10, R$1\n")
nota50 = nota20 = nota10 = nota1 = total = 0

total = int(input("Qual o valor total a ser sacado: R$ "))

while total > 0:
    if total % 50 == 0:
        nota50 += 1
        total -= 50
    elif total % 20 == 0:
        nota20 += 1
        total -= 20
    elif total % 10 == 0:
        nota10 += 1
        total -= 10
    elif total % 1 == 0:
        nota1 += 1
        total -= 1

print("\nVocê receberá: ")
if nota50 != 0: print(nota50, "cédulas de R$ 50,00")
if nota20 != 0: print(nota20, "cédulas de R$ 20,00")
if nota10 != 0: print(nota10, "cédulas de R$ 10,00")
if nota1 != 0: print(nota1, "cédulas de R$ 1,00")

print("\nVOLTE SEMPRE!!!\n")
