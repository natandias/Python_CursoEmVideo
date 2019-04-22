

#confere se é numerico
num3 = input ("Retorna TRUE se for numero:  ")
print (num3.isnumeric())

#confere se é letra
num4 = input ("Retorna TRUE se for letra:  ")
print (num3.isalpha())

#confere se é letra ou numero
num5 = input ("Retorna TRUE se for numero ou letra:  ")
print (num3.isalnum())

nome = str(input('Qual seu nome? '))

##print ("Nice to meet you {:<20}!".format(nome))
print ("Nice to meet you {:>20}!".format(nome))
print ("Nice to meet you {:^20}!".format(nome))
print ("Nice to meet you {:=^20}!".format(nome))