from datetime import datetime


def area(larg, compr):
    area = larg * compr
    return area


print()
print("CÁLCULO DE AREA DE TERRENO ------ ", datetime.now().strftime('%H:%M'))
print("="*40)
larg = float(input("Digite a largura do terreno (M): "))
compr = float(input("Digite o comprimento do terreno (M): "))
print(F"A area do terreno é: {area(larg, compr)} m²")
