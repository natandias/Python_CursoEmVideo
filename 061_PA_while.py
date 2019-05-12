pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
i=0
termos_pa = []
termo = pt

while i<10:
    i+=1
    termos_pa.append(termo)    
    termo += razao

print ("\nDez primeiros termos da PA: ")
for k in termos_pa:
    print (k, end = ' ')

mais = int(input('''\n\nDeseja imprimir mais alguns termos ?? Se sim, quantos? ''' ))
while mais != 0:
    termos_pa.append (termo)
    termo += razao
    mais -= 1

print (f"A sequência com {len(termos_pa)} termos da PA é: ")
for k in termos_pa:
    print (k, end = ' ')
print ("\n")