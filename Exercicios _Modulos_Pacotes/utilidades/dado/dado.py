def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def leiaDinheiro(entrada):
    entrada = entrada.replace(',', '.')
    if entrada.isnumeric() or isFloat(entrada):
        entrada = float(entrada)
        return entrada
    else:
        print('Esse não é um numero')
        ret = leiaDinheiro(input('Digite um numero: '))
    return ret
