words_ini = ('Dançarina', 'Amanhecer', 'Trazer', 'Oceano',
             'Alpes', 'Casaco', 'Vergonha', 'Tanque')

words = (words_ini[0].upper(), words_ini[1].upper(), words_ini[2].upper(),
         words_ini[3].upper(), words_ini[4].upper(), words_ini[5].upper(),
         words_ini[6].upper(), words_ini[7].upper())

print("\n")
for i in range(0, len(words_ini)):
    print(f"Na palavra {words[i]} temos as vogais: ", end=' ')
    if 'A' in words[i]:
        print('a', end=' ')
    if 'E' in words[i]:
        print('e', end=' ')
    if 'I' in words[i]:
        print('i', end=' ')
    if 'O' in words[i]:
        print('o', end=' ')
    if 'U' in words[i]:
        print('u', end=' ')
    print("\t")
print("\n")
