num = int(input("De qual numero você quer a tabuada? "))

print ('-='*8, 'TABUADA DE', num, '+='*8)

for i in range (1, 11):
    if i<10:  
        print (f"{num} *  {i}  = ", i*num)
    else: 
        print (f"{num} * {i}  = ", i*num)


