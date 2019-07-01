def voto(ano):
    from datetime import date
    idade = int(date.today().strftime('%Y')) - ano
    if idade >= 18 and idade < 65:
        return (f'Com {idade} anos: Voto obrigatório')
    elif idade >= 16 or idade >= 65:
        return (f'Com {idade} anos: Voto opcional')
    else:
        return (f'Com {idade} anos: Não vota')


print('--'*15)
ano_nasc = int(input('Você nasceu em qual ano: '))
while ano_nasc < 1900:
    ano_nasc = int(input('Digite um ano maior que 1899: '))
print(voto(ano_nasc))
print('--'*15, '\n')
