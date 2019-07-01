''' Interactive Help '''
# help()
# pode-se consultar a documentação da linguagem de forma otimizada

# print(input.__doc__)
# mostra informações sobre o método
''' docstring '''
# exibe informações sobre as funções criadas por você. Ex:


def contador(i, f, p):
    """ 
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print("FIM")


print()
# help(contador)
contador(5, 10, 1)

''' Argumentos(parâmetros) opcionais '''
# Ex: nessa função, se o C não for informado, ele terá valor 0
# se todos forem opcionais, é possivel que a função funcione sem nenhum valor


def somar(a=0, b=0, c=0):
    s = a+b+c
    print('Soma = ', s)

somar(3, 2, 5)
somar(8, 4)
print('\n')

''' Escopo de variáveis '''
# globais e locais
# se a variável for declarada no 'main', ela é global
# se a variável for declarada na função, ela é local
# variaveis globais, podem ser vistas no 'main' e nas funções
# variaveis locais só são vistas dentro das funções (parâmetros)
# importação de bibliotecas também podem ser globais ou locais
''' Para usar uma variável global dentro de uma função, é preciso
declarar global 'variavel' dentro da função '''


def teste(b):
    global a
    a = 8
    print(f'Na função teste a vale {a}')


a = 2
b = 4
print(f'No main a vale {a}')
teste(b)
print(f'No main depos da função, a vale {a}')

''' Retorno de resultados '''
# Ex: Fatorial


def fatorial(num=1):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat

print()
num = int(input('Calcular fatorial de: '))
print(fatorial(num))



