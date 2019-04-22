from datetime import date

ano = int(input('Digite o ano que deseja saber se é bissexto: '))
if ano == 0: date.today().year
if  ano%100 == 0 and ano%4 == 0:
    print ("Ano não bissexto\n")
else:  
    if ano%4 != 0:
        if ano%400 != 0:
            print ("Ano não bissexto\n")
        else: print ("Ano bissexto\n")
    else: print ("Ano bissexto\n")

