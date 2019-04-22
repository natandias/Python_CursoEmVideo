import math, time

print ("-=-"*14)
print("Analisador de Triângulos")
print ("-=-"*14)

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

end_time = time.time()+2
countTimer = 0
sleepTime = 0.2
print ("Processando. . .",end=' ')
while time.time() < end_time:
    time.sleep (sleepTime)
    countTimer += sleepTime
    print (".", end=' ')

if abs(b-c) < a < b+c:
    if abs(a-c) < b < a+c:
        if abs(a-b) < c < a+b:
            print("\nÉ possível formar um triângulo com esses segmentos\n")
else: print ("\nNão é possível formar um triângulo com esses segmentos \n")

