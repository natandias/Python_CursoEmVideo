frase = "Curso em Video Python"
#todos os comandos fazem distinçao entre MAIUSCULAS e minusculas
#frase [inicio:final:salto]
#pode-se colocar r ou l antes da função para começar pela esq ou dir

print ("Imprime uma string a partir da posição 9 até a 20: ")
print (frase[9:21])

print ("\n")
print ("Imprime uma string a partir da posição 9 até a 20 (saltando de 3 em 3 posições): ")
print (frase[9:21:3])

print ("\n")
print ("Imprime da posição 0 até a posição 5: ")
print(frase[:5])

print ("\n")
print ("Imprime da posição 5 até ao final: ")
print(frase[5:])

print ("\n")
print ("Imprime tudo a partir da posição 5 (saltando de 2 em 2 posições): ")
print(frase[5::2])

print ("\n")
print ("Retorna comprimento da string: ")
print (len(frase))

print ("\n")
print ("Conta quantas vezes aparece uma letra (ou conjunto de letras) na string: ")
print(frase.count('o'))

print ("\n")
print ("Retorna a posição em que a frase começa, retorna -1 se não econtrar a palavra: ")
print (frase.find("o"))

print ("\n")
print ("Retorna TRUE se a palavra existe na lista: ")
print('Curso' in frase)

print ("\n")
print ("Substitui uma palavra por outra na string e retorna frase modificada: ")
nova = frase.replace ('Python', 'Android')
print (nova)

print ("\n")
print ("Coloca tudo em Maisculo: ")
print(frase.upper())

print ("\n")
print ("Coloca tudo em minusculo: ")
print(frase.lower())

print ("\n")
print ("Coloca a primeira letra da primeira palavra da frase em MAIUSCULO: ")
print(frase.capitalize()) 

print ("\n")
print ("Coloca a primeira letra de CADA PALAVRA em MAIUSCULO:  ")
print(frase.title())


print ("\n")
blankspace = "       Brasil Acima de Tudo, Deus Acima de Todos      "
print ("Remove espaços em branco dos dois lados: ")
print (blankspace.strip())

print ("\n")
print ("Remove espaços em branco da direita: ")
print (blankspace.rstrip())

print ("\n")
print ("Remove espaços em branco da esquerda: ")
print (blankspace.lstrip())

print ("\n")
print ("Separa as palavras de acordo com o separador definido (o separador padrão é espaço): ")
frase_separada = frase.split ()
print (frase.split())

print ("\n")
print ("Junta os elementos da frase de acordo com o separador definido: ")
print (' '.join(frase_separada))

print ("\n")
print ("Joga a frase toda para MAISCULO e conta quantos 'O' estão presentes: ")
print (frase.upper().count('O'))

print ("\n")
print ("Joga a frase toda para minusculo e diz em que posição começa a palavra 'video': ")
print (frase.lower().find('video'))

print ("""\nPara imprimir várias linhas de texto
use aspas triplas""")

print ("\n")