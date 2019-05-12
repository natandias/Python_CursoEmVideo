num = int(input("Deseja o fatorial de qual número: "))
num_ini = num
i = num-1
fat = 1

if num_ini == 0: fat = 1    
if num_ini == 1: fat = 1 
if num_ini == 2: fat = 2

while i != 1 and num_ini != 0 and num_ini != 1 and num_ini != 2:
    fat = num*i
    num = fat
    i -= 1

print (f"Fatorial de {num_ini} é igual a", fat)
