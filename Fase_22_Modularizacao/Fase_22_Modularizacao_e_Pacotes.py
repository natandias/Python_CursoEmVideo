''' Modulos servem para dividir as funcionalidades do programa e
aumentar a legibilidade do código '''
# Funções estão no arquivo funcoes.py
from uteis import numeros
# é necessário tomar cuidado para que não haja conflitos
# ex: se houver duas funções fatorial
# se houver duas funções, vai prevalecer a que foi importada por ultimo
numeros.func.fatorial(6)
num = int(input('Valor: '))
print(f'{num}! = {func.fatorial(num)}')
print(f'2 * {num} = {func.dobro(num)}')


''' Pacote é uma pasta com modulos '''
''' Pode-se manter os módulos mais organizados, separando-os por assunto '''
''' Ex: um pacote para tratamento de dados, pode conter pastas que contém
modulos para tratamento de dados por tipo de dado, como str, numeros, listas'''
''' Pode-se importar só os modulos desejados.
    Ex: from tratamento import trata_numeros '''
''' TODAS as pastas de um pacote devem conter um arquivo __init__.py '''
