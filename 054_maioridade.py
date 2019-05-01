idade = []
qts_maiores = 0
for i in range (1, 8):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    if idade >= 21:
        qts_maiores += 1

if qts_maiores == 7:
    print ("Todas as 7 pessoas já atingiram a maioridade\n")
else: 
    if qts_maiores == 1:
        print (f"{qts_maiores} pessoa atingiu a maioridade")
        print (f"{7 - qts_maiores} pessoas ainda não atingiram a maioridade\n")
    elif 7-qts_maiores == 1:
        print (f"{qts_maiores} pessoas atingiram a maioridade")
        print (f"{7 - qts_maiores} pessoa ainda não atingiu a maioridade\n")
    
    
