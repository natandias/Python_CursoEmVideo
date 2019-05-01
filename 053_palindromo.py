import unidecode

print ('--'*10, 'PALINDROMOS', '--'*10)
frase = str(input("Digite a frase e descobriremos se é um palíndromo: \n")).strip().lower()

frase = unidecode.unidecode(frase)
frase = frase.split()

frase_junta = ''
for i in frase:
    frase_junta += i

inverso = frase_junta[len(frase_junta)-1:: -1]

frase_inversa = ''
print ("\nEssa frase ao contrário é: ")
for j in range (len(frase)-1, -1, -1):
    frase_inversa += frase[j][len(frase[j])::-1]+' '
print (frase_inversa)
print ('\n')


if inverso == frase_junta:
    print ('É UM PALINDROMO !!!')
else:
    print ('NÃO É')
