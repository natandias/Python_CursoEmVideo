qtd_termos = int(input('Quantos termos da sequência de Fibonacci você deseja: '))
i = 0
fibo = []


while i < qtd_termos:
    if i == 0: termo = 0
    elif i == 1: termo = 1
    elif i == 2: termo = 1
    
    else:
        termo = fibo[i-1]+fibo[i-2]
    
    fibo.append(termo)
    i += 1 

for k in fibo:
    print (k, end = ' ')