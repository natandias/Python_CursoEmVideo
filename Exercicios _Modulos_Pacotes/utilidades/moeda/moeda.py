def dobro(valor, show=False):
    """
    Retorna o dobro do valor informado.
    :param valor: valor que será dobrado.
    :return: dobro do valor.
    """
    ret = valor * 2
    if show is True:
        return moeda(ret)
    else:
        return ret


def metade(valor, show=False):
    """
    Retorna a metade do valor informado.
    :param valor: valor que será dividido.
    :return: metade do valor.
    """
    ret = (valor/2)
    if show is True:
        return moeda(ret)
    else:
        return ret


def aumentar(valor, aumento, show=False):
    """
    Aumenta o valor de acordo com a porcentagem de aumento informada.
    :param valor: valor a ser aumentado.
    :param reducao: porcentagem de aumento.
    :return: valor aumentado.
    """
    ret = valor + (valor * (aumento/100))
    if show is True:
        return moeda(ret)
    else:
        return ret


def diminuir(valor, reducao, show=False):
    """
    Reduz o valor de acordo com a porcentagem de redução informada.
    :param valor: valor a ser reduzido.
    :param reducao: porcentagem de redução.
    :return: valor reduzido.
    """
    ret = valor - (valor*(reducao/100))
    if show is True:
        return moeda(ret)
    else:
        return ret


def moeda(valor):
    """
    Formata o valor recebido
    :param valor: recebe o valor a ser formato
    :return: valor convertido
    """
    return f'R$ {valor :.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    """
    Retorna um resumo, com dobro, metade, aumento e redução
    :param valor: valor que será analisado
    :param aumento: porcentagem em que o valor será aumentado
    :param reducao: porcentagem em que o valor será reduzido
    """
    print('='*30)
    print(' '*10, 'RESUMO', ' '*10)
    print('='*30)
    print(f'Preço analisado: {moeda(valor)}')
    print(f'Dobro do preço: {moeda(dobro(valor))}')
    print(f'Metade do preço: {moeda(metade(valor))}')
    print(f'{aumento}% do preço: {moeda(aumentar(valor, aumento))}')
    print(f'{reducao}% do preço: {moeda(diminuir(valor, reducao))}')
