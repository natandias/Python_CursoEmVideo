def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um numero.
    :param num: O numero a ser calculado o fatorial.
    :param show: opcional, mostra ou não a operação realizada
    :return: resultado da operação
    """
    fat = 1
    for c in range(1, num+1):
        fat *= c
    return fat


def dobro(num):
    return num*2
