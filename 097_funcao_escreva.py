def escreva(msg):
    msg = ' '*3 + msg + ' '*3
    print('~'*len(msg))
    print(msg)
    print('~'*len(msg))


escreva('Olá, Mundo!')
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
print()
escreva(str(input('Insira texto para testar: ')))
